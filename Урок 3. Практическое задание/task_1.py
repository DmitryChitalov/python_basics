"""
Задача 1.
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.
Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

# заводим список времен года
season_list = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето',
               'лето', 'осень', 'осень', 'осень', 'зима']
# заводим словарь времен года
season_dict = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна',
               6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень', 10: 'осень',
               11: 'осень', 12: 'зима'}

try:  # Валидация вводимых данных
    month = int(input("Введите номер месяца: "))
except ValueError:
    print("Введены неверные данные")
else:  # Проверяем, что номер месяца в нужном диапазоне
    if 0 < month <= 12:
        print("Результат через список: {}".format(season_list[month - 1]))
        print("Результат через словарь: {}".format(season_dict[month]))
    else:
        print("Введен неверный номер месяца")
