"""
Fine-tuning script for DistilBERT model using Yelp reviews dataset.
DistilBERT is optimized for web deployment and provides a good balance of performance and size.
"""

import os
import logging
from datasets import load_dataset
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    TrainingArguments,
    Trainer,
    DataCollatorWithPadding
)
import torch
import traceback

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Constants
MODEL_NAME = "distilbert-base-uncased"  # Changed to DistilBERT
OUTPUT_DIR = "models/finetuned_distilbert"
DATASET_NAME = "yelp_review_full"

def preprocess(examples, tokenizer):
    """Tokenize the texts and prepare for training."""
    return tokenizer(
        examples["text"],
        padding="max_length",
        truncation=True,
        max_length=128,
        return_tensors="pt"
    )

def main():
    """Main training function."""
    try:
        logger.info("Starting fine-tuning process...")
        
        # Load dataset
        logger.info(f"Loading dataset: {DATASET_NAME}")
        dataset = load_dataset(DATASET_NAME)
        
        # Load tokenizer
        logger.info(f"Loading tokenizer: {MODEL_NAME}")
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        
        # Tokenize dataset (do NOT remove 'label' column)
        logger.info("Tokenizing dataset...")
        tokenized_datasets = dataset.map(
            lambda x: preprocess(x, tokenizer),
            batched=True
        )
        
        # Add labels (do NOT try to remove 'label' column)
        tokenized_datasets = tokenized_datasets.map(
            lambda x: {"labels": x["label"]},
        )
        
        # Load model
        logger.info(f"Loading model: {MODEL_NAME}")
        model = AutoModelForSequenceClassification.from_pretrained(
            MODEL_NAME,
            num_labels=5  # Yelp reviews have 5 star ratings
        )
        
        # Create data collator
        data_collator = DataCollatorWithPadding(tokenizer=tokenizer)
        
        # Training arguments
        training_args = TrainingArguments(
            output_dir=OUTPUT_DIR,
            num_train_epochs=3,
            per_device_train_batch_size=16,  # Increased batch size as DistilBERT is smaller
            per_device_eval_batch_size=16,
            warmup_steps=500,
            weight_decay=0.01,
            logging_dir="./logs",
            logging_steps=100,
            save_total_limit=2,
            no_cuda=True,  # Force CPU usage
            dataloader_num_workers=1,
            dataloader_pin_memory=False,
            report_to="none"
        )
        
        # Initialize trainer
        trainer = Trainer(
            model=model,
            args=training_args,
            train_dataset=tokenized_datasets["train"],
            eval_dataset=tokenized_datasets["test"],
            data_collator=data_collator,
            tokenizer=tokenizer
        )
        
        # Start training
        logger.info("Starting training...")
        trainer.train()
        
        # Save model
        logger.info(f"Saving model to {OUTPUT_DIR}")
        trainer.save_model(OUTPUT_DIR)
        tokenizer.save_pretrained(OUTPUT_DIR)
        
        logger.info("Training completed successfully!")
        
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        logger.error(traceback.format_exc())
        raise

if __name__ == "__main__":
    main()
