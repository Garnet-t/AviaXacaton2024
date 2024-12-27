from transformers import pipeline
from typing import List, Dict

class ReviewClassifier:
    def __init__(self, model_name: str = "distilbert-base-uncased", labels: List[str] = None):
        self.labels = labels if labels else ["Претензия", "Предложение", "Благодарность"]
        self.pipeline = pipeline("text-classification", model=model_name, return_all_scores=True)
    
    def classify_reviews(self, reviews: List[Dict]) -> Dict[str, int]:
        categories_count = {label: 0 for label in self.labels}
        
        for review in reviews:
            full_text = f"{review['title']} {review['text']}"
            predictions = self.pipeline(full_text)
            
            # Find the label with the highest score
            max_label = max(predictions[0], key=lambda x: x['score'])['label']
            
            # Update the count if the label matches predefined categories
            if max_label in self.labels:
                categories_count[max_label] += 1
        
        return categories_count
