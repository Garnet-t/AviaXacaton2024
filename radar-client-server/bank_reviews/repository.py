from .models import BankReview, get_engine, get_session
from .reviews import fetch_reviews
from datetime import datetime, timedelta
import json


def save_reviews_to_db(bank_id: int, db_session):
    reviews_json = fetch_reviews(bank_id)
    reviews = json.loads(reviews_json)

    now = datetime.now()
    half_day_ago = now - timedelta(hours=12)
    saved_reviews = []

    for review in reviews:
        review_date = datetime.fromisoformat(review['date'])
        if review_date >= half_day_ago:
            db_review = BankReview(
                bank_id=bank_id,
                title=review['title'],
                text=review['text'],
                review_date=review_date,
                rating=review['rating']
            )
            db_session.add(db_review)
            saved_reviews.append(review)

    db_session.commit()
    return json.dumps(saved_reviews, ensure_ascii=False, indent=4)
