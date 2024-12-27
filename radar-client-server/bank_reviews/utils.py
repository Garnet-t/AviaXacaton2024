from datetime import datetime

def parse_review_date(date_str: str) -> datetime:
    return datetime.fromisoformat(date_str)
