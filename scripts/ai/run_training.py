"""
Run the complete training pipeline:
1. Process website content
2. Train model on GCP
3. Save and upload model
"""

import os
import logging
from pathlib import Path
from dotenv import load_dotenv
from data.content_processor import ContentProcessor
from models.train_on_gcp import GCPTrainer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    # Load environment variables
    load_dotenv()
    
    # Verify GCP configuration
    project_id = os.getenv("GCP_PROJECT_ID")
    bucket_name = os.getenv("GCP_BUCKET_NAME")
    
    if not project_id or not bucket_name:
        raise ValueError("GCP_PROJECT_ID and GCP_BUCKET_NAME environment variables must be set")
    
    # Process content
    logger.info("Processing website content...")
    processor = ContentProcessor()
    content = processor.collect_content()
    training_data = processor.format_for_training(content)
    
    # Save processed data
    output_dir = Path("data/processed")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    import json
    training_data_path = output_dir / "training_data.json"
    with open(training_data_path, 'w', encoding='utf-8') as f:
        json.dump(training_data, f, indent=2, ensure_ascii=False)
    
    logger.info(f"Processed {len(content)} content items into {len(training_data)} training examples")
    
    # Train model
    logger.info("Starting model training on GCP...")
    trainer = GCPTrainer(project_id=project_id, bucket_name=bucket_name)
    trainer.train_model(
        model_id="microsoft/phi-2",  # You can change this to other models
        training_data_path=str(training_data_path),
        output_dir="models/finetuned_phi",
        num_train_epochs=3,
        per_device_train_batch_size=4,
        gradient_accumulation_steps=4,
        learning_rate=2e-5,
        max_steps=1000
    )
    
    logger.info("Training pipeline completed successfully!")

if __name__ == "__main__":
    main() 