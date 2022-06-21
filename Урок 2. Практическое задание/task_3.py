"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

""" list """

season = ("зима", "весна", "лето", "осень")
month_index = [(12, 1 ,2), (3, 4, 5), (6, 7, 8), (9, 10, 11)]
season_name = None

month_number= int(input("Введите число месяца: "))

for ind, item in enumerate(month_index):
    if month_number in item:
        season_name = season[ind]

print(f"Результат через список: {season_name}")


""" dict """
month_number= int(input("Введите число месяца: "))
season = {"зима":[12, 1, 2], "весна": [3, 4, 5], "лето": [6, 7, 8], "осень": [9, 10, 11] }
for key, value in season.items():
    if month_number in value:
        season_name = key

print(f"Результат через словарь: {season_name}")