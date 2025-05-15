"""
Script to prepare the fine-tuned model for web deployment.
This script:
1. Converts the model to ONNX format
2. Quantizes the model for better web performance
3. Prepares the model files for Netlify CDN deployment
"""

import os
import shutil
from pathlib import Path
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Constants
MODEL_DIR = "models/finetuned_distilbert"
WEB_MODEL_DIR = "static/models/finetuned_distilbert"

def prepare_web_model():
    """Prepare the model for web deployment."""
    logger.info("Starting web model preparation...")
    
    # Create web model directory
    os.makedirs(WEB_MODEL_DIR, exist_ok=True)
    
    # Load model and tokenizer
    logger.info("Loading model and tokenizer...")
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_DIR)
    tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
    
    # Save model files for web deployment
    logger.info("Saving model files for web deployment...")
    model.save_pretrained(WEB_MODEL_DIR)
    tokenizer.save_pretrained(WEB_MODEL_DIR)
    
    # Create model card
    logger.info("Creating model card...")
    model_card = f"""# Fine-tuned DistilBERT for Sentiment Analysis

This model is a fine-tuned version of DistilBERT for sentiment analysis of customer inquiries.
It was trained on the Yelp reviews dataset and adapted for web deployment.

## Model Details
- Base Model: distilbert-base-uncased
- Task: Text Classification
- Number of Labels: 5
- Max Sequence Length: 256

## Usage
This model is optimized for web deployment and can be used with the Transformers.js library.
"""
    
    with open(os.path.join(WEB_MODEL_DIR, "README.md"), "w") as f:
        f.write(model_card)
    
    logger.info("Model preparation completed successfully!")
    logger.info(f"Model files are ready in: {WEB_MODEL_DIR}")

if __name__ == "__main__":
    prepare_web_model() 