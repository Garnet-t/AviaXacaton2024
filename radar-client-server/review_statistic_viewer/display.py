from .statistic import ReviewStatistic

class ReviewStatisticViewer:
    def __init__(self, categories: dict[str, int]):
        self.statistic = ReviewStatistic(categories)
    
    def display_table(self):
        table = self.statistic.generate_table()
        print(table)
    
    def display_pie_chart(self):
        self.statistic.generate_pie_chart()
    
    def display_bar_chart(self):
        self.statistic.generate_bar_chart()
