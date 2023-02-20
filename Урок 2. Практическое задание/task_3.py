"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
saesons_dict = {1 : 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
month = int(input("Введите номер месяца "))
if month ==12 or month<=2:
    print(saesons_dict.get(1))
    print(seasons_list[0])
elif month ==3 or month<=5:
    print(saesons_dict.get(2))
    print(seasons_list[1])
elif month ==6 or month<=8:
    print(saesons_dict.get(3))
    print(seasons_list[2])
elif month ==9 or month<=11:
    print(saesons_dict.get(4))
    print(seasons_list[3])
else:
    print("Нет такого месяца")
