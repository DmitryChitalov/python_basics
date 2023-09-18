"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

# через list
month = int(input("Введите номер месяца: "))

while month > 12:
    month = int(input("Введите номер месяца коректно: "))

season = ['Winter', 'Spring', 'Summer', 'Autumn']

if month in [12, 2, 1]:
    print(f"Результ: {season[0]}")

if month in [3, 4, 5]:
    print(f"Результ: {season[1]}")

if month in [6, 7, 8]:
    print(f"Результ: {season[2]}")

if month in [9, 10, 11]:
    print(f"Результ: {season[3]}")

# через dict
month = int(input("Введите номер месяца: "))

while month > 12:
    month = int(input("Введите номер месяца коректно: "))

season = {1: 'Winter', 2: 'Summer', 3: 'Spring', 4: 'Autumn'}

if month in [12, 2, 1]:
    print(season.get(1))

if month in [3, 4, 5]:
    print(season.get(2))

if month in [6, 7, 8]:
    print(season.get(3))

if month in [9, 10, 11]:
    print(season.get(4))
