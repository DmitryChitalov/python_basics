"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

season_list = ('Winter', 'Winter',
                'Spring', 'Spring', 'Spring',
                'Summer', 'Summer', 'Summer',
                'Autumn', 'Autumn', 'Autumn',
                'Winter')
season_dict = {str(k): v for (k, v) in enumerate(season_list, 1)}
month_str = int(input("Введите номер месяца от 1 до 12 - "))
month = int(month_str)
if month in range(1, 13):
    print(season_list[month - 1])
else:
    print("Такого месяца не существет")
print(season_dict.get(month_str) or "Такого месяца не существует")
