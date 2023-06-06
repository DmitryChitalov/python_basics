class Date:
    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod
    def extract_values(cls, date_str):
        day, month, year = map(int, date_str.split('-'))
        return day, month, year

    @staticmethod
    def validate_date(day, month, year):
        if 1 <= day <= 31 and 1 <= month <= 12:
            return True
        else:
            return False

# Пример использования
date_str = "25-05-2023"

day, month, year = Date.extract_values(date_str)
if Date.validate_date(day, month, year):
    print("Дата валидна")
else:
    print("Неверная дата")
