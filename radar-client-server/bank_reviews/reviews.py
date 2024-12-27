import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from .utils import parse_review_date
import json

def fetch_recent_reviews(bank_id: int):
    base_url = f"https://www.banki.ru/services/responses/bank/{bank_id}/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    response = requests.get(base_url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Ошибка при запросе страницы: {response.status_code}")
    
    soup = BeautifulSoup(response.text, 'html.parser')
    review_containers = soup.find_all('div', class_='responses__item')
    reviews = []
    now = datetime.now()
    half_day_ago = now - timedelta(hours=12)

    for container in review_containers:
        try:
            title = container.find('a', class_='header-h3').text.strip()
            text = container.find('div', class_='responses__item__message').text.strip()
            date_str = container.find('time')['datetime']
            date = parse_review_date(date_str)
            
            if date >= half_day_ago:
                rating = container.find('span', class_='rating-grade').text.strip() if container.find('span', class_='rating-grade') else None
                reviews.append({
                    "title": title,
                    "text": text,
                    "date": date_str,
                    "rating": rating
                })
        except Exception as e:
            print(f"Ошибка при обработке контейнера: {e}")

    return json.dumps(reviews, ensure_ascii=False, indent=4)
