"""
Fine-tuning script for the Phi-1.5 model using markdown content.
"""

import os
import json
from pathlib import Path
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer
from datasets import Dataset
import torch
from tqdm import tqdm

# Constants
MODEL_NAME = "microsoft/phi-2"
OUTPUT_DIR = "models/finetuned_phi"
CONTENT_DIR = "content"

def collect_markdown_content():
    """Collect all markdown content from the content directory."""
    qa_pairs = []
    
    def process_markdown_file(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Split content into sections
        sections = content.split('\n\n')
        current_section = ""
        
        for section in sections:
            if section.startswith('#'):
                # This is a heading, use it as a question
                question = section.strip('#').strip()
                if current_section:
                    qa_pairs.append({
                        "question": question,
                        "answer": current_section.strip()
                    })
                current_section = ""
            else:
                current_section += section + "\n\n"
    
    # Process all markdown files in content directory and subdirectories
    for root, dirs, files in os.walk(CONTENT_DIR):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                print(f"Processing {file_path}")
                process_markdown_file(file_path)
                print(f"Processed {file_path}: {len(qa_pairs)} Q&A pairs")
    
    return qa_pairs

def preprocess(examples, tokenizer):
    """Preprocess the examples for training."""
    input_texts = []
    for q, a in zip(examples["question"], examples["answer"]):
        input_texts.append(f"Question: {q}\nAnswer: {a}")
    
    tokenized = tokenizer(input_texts, padding="max_length", truncation=True, max_length=512)
    return tokenized

def main():
    # Create output directory if it doesn't exist
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Collect training data
    print("🧹 Collecting markdown content...")
    qa_pairs = collect_markdown_content()
    print(f"📚 Loaded {len(qa_pairs)} Q&A pairs for training.")
    
    # Convert to dataset
    dataset = Dataset.from_dict({
        "question": [pair["question"] for pair in qa_pairs],
        "answer": [pair["answer"] for pair in qa_pairs]
    })
    
    # Load model and tokenizer
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    
    # Set padding token
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
        model.config.pad_token_id = tokenizer.eos_token_id
    
    # Preprocess dataset
    tokenized_dataset = dataset.map(lambda x: preprocess(x, tokenizer), batched=True)
    
    # Training arguments
    training_args = TrainingArguments(
        output_dir=OUTPUT_DIR,
        num_train_epochs=3,
        per_device_train_batch_size=4,
        save_steps=100,
        save_total_limit=2,
        logging_steps=10,
        learning_rate=2e-5,
        weight_decay=0.01,
        warmup_steps=100,
    )
    
    # Initialize trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
    )
    
    # Train the model
    print("🚀 Starting training...")
    trainer.train()
    
    # Save the model
    print("💾 Saving model...")
    trainer.save_model()
    tokenizer.save_pretrained(OUTPUT_DIR)
    
    print("✅ Training complete!")

if __name__ == "__main__":
    main() 