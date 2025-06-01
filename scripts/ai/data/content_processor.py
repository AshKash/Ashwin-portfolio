"""
Process website content for model training.
Collects and processes all posts and pages from the Hugo website.
"""

import os
from pathlib import Path
from typing import List, Dict, Any
import frontmatter
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ContentProcessor:
    def __init__(self, content_dir: str = "content"):
        self.content_dir = content_dir
        self.posts_dir = os.path.join(content_dir, "posts")
        self.pages_dir = os.path.join(content_dir, "pages")
    
    def process_markdown(self, file_path: str) -> Dict[str, Any]:
        """Process a markdown file and extract content and metadata."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
                
            return {
                'path': file_path,
                'title': post.metadata.get('title', ''),
                'description': post.metadata.get('description', ''),
                'content': post.content,
                'tags': post.metadata.get('tags', []),
                'categories': post.metadata.get('categories', []),
                'date': post.metadata.get('date', '')
            }
        except Exception as e:
            logger.error(f"Error processing {file_path}: {str(e)}")
            return None

    def collect_content(self) -> List[Dict[str, Any]]:
        """Collect all content from posts and pages."""
        content = []
        
        # Process posts
        for root, _, files in os.walk(self.posts_dir):
            for file in files:
                if file.endswith('.md'):
                    file_path = os.path.join(root, file)
                    processed = self.process_markdown(file_path)
                    if processed:
                        content.append(processed)
        
        # Process pages
        for root, _, files in os.walk(self.pages_dir):
            for file in files:
                if file.endswith('.md'):
                    file_path = os.path.join(root, file)
                    processed = self.process_markdown(file_path)
                    if processed:
                        content.append(processed)
        
        return content

    def format_for_training(self, content: List[Dict[str, Any]]) -> List[Dict[str, str]]:
        """Format content for model training."""
        training_data = []
        
        for item in content:
            # Create instruction-response pairs
            instruction = f"Write content about {item['title']}"
            response = f"Title: {item['title']}\n\n{item['content']}"
            
            training_data.append({
                'instruction': instruction,
                'response': response
            })
            
            # Add category-based examples
            if item['categories']:
                for category in item['categories']:
                    instruction = f"Write content about {category}"
                    response = f"Title: {item['title']}\n\n{item['content']}"
                    training_data.append({
                        'instruction': instruction,
                        'response': response
                    })
            
            # Add tag-based examples
            if item['tags']:
                for tag in item['tags']:
                    instruction = f"Write content about {tag}"
                    response = f"Title: {item['title']}\n\n{item['content']}"
                    training_data.append({
                        'instruction': instruction,
                        'response': response
                    })
        
        return training_data

def main():
    processor = ContentProcessor()
    content = processor.collect_content()
    training_data = processor.format_for_training(content)
    
    # Save processed data
    output_dir = "data/processed"
    os.makedirs(output_dir, exist_ok=True)
    
    import json
    with open(os.path.join(output_dir, "training_data.json"), 'w', encoding='utf-8') as f:
        json.dump(training_data, f, indent=2, ensure_ascii=False)
    
    logger.info(f"Processed {len(content)} content items into {len(training_data)} training examples")

if __name__ == "__main__":
    main() 