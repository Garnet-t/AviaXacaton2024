import unittest
from bank_reviews.reviews import fetch_recent_reviews
from unittest.mock import patch
import json

class TestFetchReviews(unittest.TestCase):
    
    @patch('bank_reviews.reviews.requests.get')
    def test_fetch_recent_reviews(self, mock_get):
        # Мокируем успешный ответ от requests.get
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = '''
        <html>
            <body>
                <div class="responses__item">
                    <a class="header-h3">Отличный сервис</a>
                    <div class="responses__item__message">Очень доволен!</div>
                    <time datetime="2024-12-23T10:00:00">2024-12-23</time>
                    <span class="rating-grade">5</span>
                </div>
                <div class="responses__item">
                    <a class="header-h3">Не понравилось</a>
                    <div class="responses__item__message">Банк обманул</div>
                    <time datetime="2024-12-23T11:00:00">2024-12-23</time>
                    <span class="rating-grade">1</span>
                </div>
            </body>
        </html>
        '''
        
        # Выполняем функцию парсинга
        reviews_json = fetch_recent_reviews(13)
        
        # Проверяем, что ответ - это список отзывов в формате JSON
        reviews = json.loads(reviews_json)
        
        # Печатаем полученные данные
        print("Полученные отзывы:")
        for review in reviews:
            print(f"Название: {review['title']}")
            print(f"Текст: {review['text']}")
            print(f"Дата: {review['date']}")
            print(f"Рейтинг: {review['rating']}")
            print("-" * 50)
        
        # Проверяем, что отзывы парсятся корректно
        self.assertEqual(len(reviews), 2)
        self.assertEqual(reviews[0]['title'], 'Отличный сервис')
        self.assertEqual(reviews[0]['rating'], '5')
        self.assertEqual(reviews[1]['title'], 'Не понравилось')
        self.assertEqual(reviews[1]['rating'], '1')
    
    @patch('bank_reviews.reviews.requests.get')
    def test_fetch_reviews_no_reviews(self, mock_get):
        # Мокируем ответ, если отзывов нет
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = '''
        <html>
            <body></body>
        </html>
        '''
        
        # Выполняем функцию парсинга
        reviews_json = fetch_recent_reviews(13)
        
        # Проверяем, что возвращается пустой список
        reviews = json.loads(reviews_json)
        
        # Печатаем полученные данные (ничего не должно быть)
        print("Полученные отзывы (не должно быть отзывов):")
        for review in reviews:
            print(f"Название: {review['title']}")
            print(f"Текст: {review['text']}")
            print(f"Дата: {review['date']}")
            print(f"Рейтинг: {review['rating']}")
            print("-" * 50)

        self.assertEqual(len(reviews), 0)

if __name__ == '__main__':
    unittest.main()
