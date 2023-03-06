"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

user_input = int(input('Введите номер месяца: '))

# Вариант через list

month_list = [['Зима', 12, 1, 2], ['Весна', 3, 4, 5], ['Лето', 6, 7, 8], ['Осень', 9, 10, 11]]

for el in month_list:
    if user_input in el:
        print(f'Результат через список: {el[0]}')

# Вариант через dict

month_dict = {'Зима': [12, 1, 2],
              'Весна': [3, 4, 5],
              'Лето': [6, 7, 8],
              'Осень': [9, 10, 11]}

for el in month_dict.items():
    if user_input in el[1]:
        print(f'Результат через словарь: {el[0]}')
