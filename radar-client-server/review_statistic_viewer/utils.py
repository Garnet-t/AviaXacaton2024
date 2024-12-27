from typing import Dict

def aggregate_categories(classification_results: list) -> Dict[str, int]:
    aggregated = {}
    for result in classification_results:
        for category, count in result.items():
            aggregated[category] = aggregated.get(category, 0) + count
    return aggregated
