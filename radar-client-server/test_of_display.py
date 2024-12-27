from review_statistic_viewer.display import ReviewStatisticViewer
from review_statistic_viewer.utils import aggregate_categories

# Пример: результаты классификации из первого пакета
classification_results = [
    {"Претензия": 1, "Предложение": 0, "Благодарность": 0},
    {"Претензия": 0, "Предложение": 1, "Благодарность": 0},
    {"Претензия": 0, "Предложение": 0, "Благодарность": 1},
]

# Объединение результатов
aggregated_categories = aggregate_categories(classification_results)

# Отображение статистики
viewer = ReviewStatisticViewer(aggregated_categories)

# Печать таблицы
viewer.display_table()

# Печать диаграммы
viewer.display_pie_chart()
viewer.display_bar_chart()
