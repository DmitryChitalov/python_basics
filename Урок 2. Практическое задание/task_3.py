"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""
number = input("Введите число месяца ===>   ")
# исключение, что бы не ввели символы
try:
    number = int(number)
    print("Месяц введен верно")
except ValueError:
    print("Не верный формат ввода")
if number > 12:
    print("Не верно введено число")
else:
    month = ["Зима", "Весна", "Лето", "Осень"]
    if number <= 5 or number == 12:
        if number <= 2 or number == 12:
            print((number), "явлеяется месяцем", month[0])
        else:
            print((number), "явлеяется месяцем", month[1])
    else:
        if number <= 8:
            print((number), "явлеяется месяцем", month[2])
        else:
            print((number), "явлеяется месяцем", month[3])
    # часть с словарями
    month = {1: "Зима", 2: "Весня", 3: "Лето", 4: "Оень"}
    if number <= 5 or number == 12:
        if number <= 2 or number == 12:
            print((number), "явлеяется месяцем", month.get(1))
        else:
            print((number), "явлеяется месяцем", month.get(2))
    else:
        if number <= 8:
            print((number), "явлеяется месяцем", month.get(3))
        else:
            print((number), "явлеяется месяцем", month.get(4))
