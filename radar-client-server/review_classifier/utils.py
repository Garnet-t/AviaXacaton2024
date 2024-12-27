from typing import List, Dict

def preprocess_review(review: Dict) -> str:
    title = review.get("title", "").strip()
    text = review.get("text", "").strip()
    return f"{title}. {text}".strip()

def validate_reviews(reviews: List[Dict]) -> List[Dict]:
    valid_reviews = []
    for review in reviews:
        if not isinstance(review, dict):
            continue
        if "title" in review and "text" in review and "date" in review and "rating" in review:
            valid_reviews.append(review)
    return valid_reviews

def aggregate_results(results: List[Dict[str, int]]) -> Dict[str, int]:
    aggregated = {}
    for result in results:
        for label, count in result.items():
            aggregated[label] = aggregated.get(label, 0) + count
    return aggregated
