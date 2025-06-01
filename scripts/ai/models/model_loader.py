"""
Model loader for AI tasks.
Handles loading and initialization of AI models.
"""

import os
from pathlib import Path
from transformers import AutoTokenizer, AutoModelForCausalLM

class ModelLoader:
    def __init__(self, model_dir: str = None):
        self.model_dir = model_dir or os.getenv('MODEL_DIR', 'models')
        self.models = {}
        self.tokenizers = {}
    
    def load_model(self, model_name: str, model_type: str = "phi"):
        """
        Load a specific model by name and type.
        
        Args:
            model_name (str): Name of the model to load
            model_type (str): Type of model (e.g., 'phi', 'embedding', 'generation')
        """
        if model_name in self.models:
            return self.models[model_name]
            
        if model_type == "phi":
            model_path = os.path.join(self.model_dir, model_name)
            if not os.path.exists(model_path):
                raise FileNotFoundError(f"Model not found at {model_path}")
                
            self.tokenizers[model_name] = AutoTokenizer.from_pretrained(model_path)
            self.models[model_name] = AutoModelForCausalLM.from_pretrained(model_path)
        else:
            raise ValueError(f"Unsupported model type: {model_type}")
            
        return self.models[model_name]
    
    def get_model(self, model_name: str):
        """
        Get a loaded model by name.
        
        Args:
            model_name (str): Name of the model to retrieve
        """
        return self.models.get(model_name)
        
    def get_tokenizer(self, model_name: str):
        """
        Get a loaded tokenizer by name.
        
        Args:
            model_name (str): Name of the tokenizer to retrieve
        """
        return self.tokenizers.get(model_name) 