"""
Train and fine-tune models on Google Cloud Platform using Vertex AI.

Required Environment Variables:
    GCP_PROJECT_ID: Your Google Cloud project ID (e.g., 'hellocloud-460621')
    GCP_BUCKET_NAME: Name of the GCS bucket for storing models and data
    GOOGLE_APPLICATION_CREDENTIALS: Path to your GCP service account key file

Example:
    export GCP_PROJECT_ID=hellocloud-460621
    export GCP_BUCKET_NAME=ashwin-portfolio-models
    export GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account-key.json

Note: You need to:
1. Create a GCS bucket: gcloud storage buckets create gs://{GCP_BUCKET_NAME} --project={GCP_PROJECT_ID}
2. Set up a service account with Storage Admin and Vertex AI User roles
3. Download the service account key and set GOOGLE_APPLICATION_CREDENTIALS
"""

import os
import json
import logging
from datetime import datetime
from google.cloud import aiplatform
from google.cloud import storage
from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, Trainer
from datasets import Dataset
import torch

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GCPTrainer:
    def __init__(self, project_id: str, bucket_name: str, location: str = "us-central1"):
        self.project_id = project_id
        self.bucket_name = bucket_name
        self.location = location
        self.storage_client = storage.Client(project=project_id)
        self.bucket = self.storage_client.bucket(bucket_name)
        
        # Initialize Vertex AI
        aiplatform.init(project=project_id, location=location)
        
    def upload_training_data(self, local_path: str) -> str:
        """Upload training data to GCS bucket."""
        blob_name = f"training_data/{datetime.now().strftime('%Y%m%d_%H%M%S')}/training_data.json"
        blob = self.bucket.blob(blob_name)
        blob.upload_from_filename(local_path)
        return f"gs://{self.bucket_name}/{blob_name}"
    
    def prepare_dataset(self, data_path: str) -> Dataset:
        """Prepare dataset for training."""
        with open(data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Convert to Dataset format
        dataset = Dataset.from_list([
            {
                "text": f"### Instruction:\n{item['instruction']}\n\n### Response:\n{item['response']}"
            }
            for item in data
        ])
        
        return dataset
    
    def train_model(self, 
                   model_id: str = "microsoft/phi-2",
                   training_data_path: str = "data/processed/training_data.json",
                   output_dir: str = "models/finetuned_phi",
                   num_train_epochs: int = 3,
                   per_device_train_batch_size: int = 4,
                   gradient_accumulation_steps: int = 4,
                   learning_rate: float = 2e-5,
                   max_steps: int = 1000):
        """Train model on GCP."""
        try:
            # Upload training data
            logger.info("Uploading training data to GCS...")
            gcs_data_path = self.upload_training_data(training_data_path)
            
            # Prepare dataset
            logger.info("Preparing dataset...")
            dataset = self.prepare_dataset(training_data_path)
            
            # Load model and tokenizer
            logger.info(f"Loading model: {model_id}")
            tokenizer = AutoTokenizer.from_pretrained(model_id)
            model = AutoModelForCausalLM.from_pretrained(model_id)
            
            # Configure tokenizer
            tokenizer.pad_token = tokenizer.eos_token
            model.config.pad_token_id = tokenizer.eos_token_id
            
            # Tokenize dataset
            def tokenize(example):
                return tokenizer(
                    example["text"],
                    padding="max_length",
                    truncation=True,
                    max_length=512
                )
            
            tokenized_dataset = dataset.map(tokenize, remove_columns=["text"])
            
            # Training arguments
            training_args = TrainingArguments(
                output_dir=output_dir,
                num_train_epochs=num_train_epochs,
                per_device_train_batch_size=per_device_train_batch_size,
                gradient_accumulation_steps=gradient_accumulation_steps,
                learning_rate=learning_rate,
                max_steps=max_steps,
                logging_steps=10,
                save_steps=100,
                warmup_steps=100,
                weight_decay=0.01,
                fp16=True,  # Enable mixed precision training
                report_to="none"
            )
            
            # Initialize trainer
            trainer = Trainer(
                model=model,
                args=training_args,
                train_dataset=tokenized_dataset,
                tokenizer=tokenizer
            )
            
            # Start training
            logger.info("Starting training...")
            trainer.train()
            
            # Save model
            logger.info(f"Saving model to {output_dir}")
            trainer.save_model(output_dir)
            tokenizer.save_pretrained(output_dir)
            
            # Upload model to GCS
            logger.info("Uploading model to GCS...")
            model_blob_name = f"models/{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            model_blob = self.bucket.blob(model_blob_name)
            
            # Upload each file in the model directory
            for root, _, files in os.walk(output_dir):
                for file in files:
                    local_path = os.path.join(root, file)
                    remote_path = os.path.join(model_blob_name, os.path.relpath(local_path, output_dir))
                    blob = self.bucket.blob(remote_path)
                    blob.upload_from_filename(local_path)
            
            logger.info("Training completed successfully!")
            
        except Exception as e:
            logger.error(f"An error occurred during training: {str(e)}")
            raise

def main():
    # Get GCP configuration from environment variables
    project_id = os.getenv("GCP_PROJECT_ID")
    bucket_name = os.getenv("GCP_BUCKET_NAME")
    
    if not project_id or not bucket_name:
        raise ValueError("GCP_PROJECT_ID and GCP_BUCKET_NAME environment variables must be set")
    
    trainer = GCPTrainer(project_id=project_id, bucket_name=bucket_name)
    trainer.train_model()

if __name__ == "__main__":
    main() 