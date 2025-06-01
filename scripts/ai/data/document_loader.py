"""
Document loader for AI tasks.
Handles loading and processing of documents for model training or inference.
"""

import json
from pathlib import Path
from typing import List, Dict, Any

class DocumentLoader:
    def __init__(self, data_dir: str = None):
        self.data_dir = data_dir or 'data'
    
    def load_documents(self, file_paths: List[str]) -> List[Dict[str, Any]]:
        """
        Load documents from specified file paths.
        
        Args:
            file_paths (List[str]): List of file paths to load
            
        Returns:
            List[Dict[str, Any]]: List of loaded documents
        """
        documents = []
        for file_path in file_paths:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    documents.append({
                        'path': file_path,
                        'content': content,
                        'type': Path(file_path).suffix[1:]
                    })
            except Exception as e:
                print(f"Error loading {file_path}: {str(e)}")
        
        return documents
    
    def save_embeddings(self, embeddings: List[Dict[str, Any]], output_path: str):
        """
        Save document embeddings to a file.
        
        Args:
            embeddings (List[Dict[str, Any]]): List of document embeddings
            output_path (str): Path to save embeddings
        """
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(embeddings, f, indent=2) 