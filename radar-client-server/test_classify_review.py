import unittest
from review_classifier.classifier import ReviewClassifier
from bank_reviews.reviews import fetch_recent_reviews
import json

class TestReviewClassifier(unittest.TestCase):
    
    def setUp(self):
        # Инициализируем классификатор перед каждым тестом
        self.classifier = ReviewClassifier()
    
    def test_parsing_and_classifying_reviews(self):
        # Получаем отзывы с сайта для конкретного банка (например, банк с ID 123)
        bank_id = 123
        reviews_json = fetch_recent_reviews(bank_id)
        
        # Преобразуем JSON в объект Python (список словарей)
        reviews = json.loads(reviews_json)
        
        # Проверяем, что парсер вернул не пустой список отзывов
        if len(reviews) == 0:
            print("Нет отзывов для классификации.")
        else:
            # Классифицируем отзывы
            result = self.classifier.classify_reviews(reviews)
            
            # Печатаем результат классификации
            print(f"Результат классификации: {result}")
        
        # Проверка на наличие отзывов
        self.assertGreater(len(reviews), 0, "Нет отзывов для классификации")
    
    def test_empty_reviews(self):
        # Пытаемся получить отзывы с несуществующего банка (или банка с нулевыми отзывами)
        bank_id = 9999
        reviews_json = fetch_recent_reviews(bank_id)
        
        # Преобразуем JSON в объект Python (список словарей)
        reviews = json.loads(reviews_json)
        
        # Проверяем, что отзывы отсутствуют
        if len(reviews) == 0:
            print("Отзывы для этого банка пустые.")
        else:
            result = self.classifier.classify_reviews(reviews)
            print(f"Результат классификации: {result}")
        
        # Проверяем, что отзывы отсутствуют
        self.assertEqual(len(reviews), 0, "Отзывы для этого банка должны быть пустыми")
        
        # Проверяем, что для пустого списка результат будет равен нулю
        self.assertEqual(result["Претензия"], 0)
        self.assertEqual(result["Предложение"], 0)
        self.assertEqual(result["Благодарность"], 0)

if __name__ == '__main__':
    unittest.main()
