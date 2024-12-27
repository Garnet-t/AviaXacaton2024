from typing import Dict
import matplotlib.pyplot as plt
from tabulate import tabulate

class ReviewStatistic:
    def __init__(self, categories: Dict[str, int]):
        self.categories = categories

    def generate_table(self) -> str:
        headers = ["Категория", "Количество"]
        table = [(category, count) for category, count in self.categories.items()]
        return tabulate(table, headers=headers, tablefmt="grid")
    
    def generate_pie_chart(self):
        labels = list(self.categories.keys())
        sizes = list(self.categories.values())
        
        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
        plt.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title("Распределение категорий отзывов")
        plt.show()
    
    def generate_bar_chart(self):
        categories = list(self.categories.keys())
        counts = list(self.categories.values())
        
        plt.figure(figsize=(8, 6))
        plt.bar(categories, counts, color="skyblue")
        plt.title("Количество отзывов по категориям")
        plt.xlabel("Категория")
        plt.ylabel("Количество")
        plt.show()
