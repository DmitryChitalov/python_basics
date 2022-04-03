"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""
seasons_list = ["Зима", "Весна", "Лето", "Осень"]
seasons_dict = {1 : "Зима", 2 : "Весна", 3 : "Лето", 4 : "Осень"}
month = int(input("Введите месяц по номеру 1-12:"))
if month ==1 or month == 2 or month == 12:
    print("list:", seasons_dict.get(1))
    print("dict:", seasons_list[0])
elif month == 3 or month == 4 or month ==5:
    print("list:", seasons_dict.get(2))
    print("dict:", seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print("list:", seasons_dict.get(3))
    print("dict:", seasons_list[2])
elif month == 9 or month == 10 or month == 11:
    print("list:", seasons_dict.get(4))
    print("dict:", seasons_list[3])
else:
    print("Такого месяца не существует")
