"""
Self-contained script to fine-tune the `microsoft/phi-2` model using a small instruction-style dataset.
Tested on Apple M1 (CPU or MPS). Adjust batch size and length for your machine.
"""

import os
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, Trainer
from datasets import Dataset
from transformers import DataCollatorForLanguageModeling
import multiprocessing

def main():
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    torch.set_num_threads(os.cpu_count())

    examples = [
        {"instruction": "What is AI?", "response": "AI stands for Artificial Intelligence."},
        {"instruction": "Define machine learning.", "response": "Machine learning is a subset of AI that learns from data."},
        {"instruction": "Explain LLMs.", "response": "LLMs are large language models trained to generate and understand text."},
    ]

    dataset = Dataset.from_list([
        {"text": f"### Instruction:\n{e['instruction']}\n\n### Response:\n{e['response']}"} for e in examples
    ])

    model_id = "microsoft/phi-2"
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id)

    device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
    model = model.to(device)
    tokenizer.pad_token = tokenizer.eos_token
    model.config.pad_token_id = tokenizer.eos_token_id

    def tokenize(example):
        out = tokenizer(
            example["text"],
            padding="max_length",
            truncation=True,
            max_length=256
        )
        out["labels"] = out["input_ids"]
        return out

    tokenized_dataset = dataset.map(tokenize, remove_columns=["text"])

    data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

    training_args = TrainingArguments(
        output_dir="./finetuned_phi2",
        num_train_epochs=3,
        per_device_train_batch_size=1,
        gradient_accumulation_steps=2,
        logging_steps=1,
        save_strategy="epoch",
        save_total_limit=1,
        learning_rate=5e-5,
        fp16=False,
        bf16=False,
        dataloader_num_workers=2,
        report_to="none",
        disable_tqdm=False
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
        data_collator=data_collator,
    )

    trainer.train()
    trainer.save_model("./finetuned_phi2")
    tokenizer.save_pretrained("./finetuned_phi2")

if __name__ == "__main__":
    multiprocessing.set_start_method("fork", force=True)
    main()
