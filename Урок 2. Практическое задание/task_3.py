"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

month = int(input("Введите месяц по номеру "))
seasons_dict = {1 : 'зима', 2 : 'весна', 3 : 'лето', 4 : 'осень'}
seasons_list = ['зима', 'весна', 'лето', 'осень']
if 12 >= month >= 1:
    if 3 <= month <= 5:
        print(seasons_dict.get(2))
        print(seasons_list[1])
    elif 6 <= month <= 8:
        print(seasons_dict.get(3))
        print(seasons_list[2])
    elif 9 <= month <= 11:
        print(seasons_dict.get(4))
        print(seasons_list[3])
    else:
        print(seasons_dict.get(1))
        print(seasons_list[0])

else:
    print("Такого месяца не существует")
