"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

month = 0
while month > 12 or month <= 0:
    month = int(input("Введите номер месяца: "))
    if month > 12 or month <= 0:
        print("Такого месяца не существует. Попробуйте ещё раз.")

seasons_list = ['Winter', 'Sping', 'Summer', 'Autumn']
for season in seasons_list:
    if season == "Winter":
        if month == 1 or month == 2 or month == 12:
            print(f"Результат через список: {season}")
            break
    if season == "Sping":
        if month == 3 or month == 4 or month == 5:
            print(f"Результат через список: {season}")
            break
    if season == "Summer":
        if month == 6 or month == 7 or month == 8:
            print(f"Результат через список: {season}")
            break
    if season == "Autumn":
        if month == 9 or month == 10 or month == 11:
            print(f"Результат через список: {season}")
            break

seasons_dict = {'Winter': (1, 2, 12),
                'Sping': (3, 4, 5),
                'Summer': (6, 7, 8),
                'Autumn': (9, 10, 11)}
for key in seasons_dict.keys():
    if month in seasons_dict[key]:
        print(f"Результат через словарь: {key}")
