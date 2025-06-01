# AI Scripts

This directory contains Python scripts for AI-related tasks in the portfolio website.

## Directory Structure

```
scripts/ai/
├── models/           # Model loading and management
│   ├── model_loader.py
│   └── fine_tune.py  # Fine-tuning script for Phi model
├── utils/           # Utility functions and helpers
├── data/            # Data loading and processing
└── requirements.txt # Python dependencies
```

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

The scripts are organized into three main components:

1. **Model Loader** (`models/model_loader.py`):
   - Handles loading and initialization of AI models
   - Manages model caching and reuse
   - Supports fine-tuned Phi model

2. **Text Processor** (`utils/text_processor.py`):
   - Text preprocessing and tokenization
   - Text cleaning and normalization

3. **Document Loader** (`data/document_loader.py`):
   - Loads and processes documents
   - Handles document embeddings

## Fine-tuning the Phi Model

The `fine_tune.py` script fine-tunes the Microsoft Phi-1.5 model on your markdown content:

1. Run the fine-tuning script:
```bash
python models/fine_tune.py
```

2. The script will:
   - Collect all markdown files in the project
   - Extract question-answer pairs
   - Fine-tune the Phi model
   - Save the model to `static/models/finetuned_phi`

3. The fine-tuned model can then be used by the chat agent.

## Adding New Models

To add a new model:

1. Add the model files to the appropriate directory
2. Update the model loader to support the new model
3. Add any necessary preprocessing steps
4. Update the requirements if needed

## Environment Variables

- `MODEL_DIR`: Directory containing model files (default: 'models')
- `DATA_DIR`: Directory containing data files (default: 'data') 