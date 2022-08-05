"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

month_list = [[12, 1, 2], "Зима", [3, 4, 5], "Весна", [6, 7, 8], "Лето", [9, 10, 11], "Осень"]
month_dict = {"Зима": [12, 1, 2], "Весна": [3, 4, 5], "Лето": [6, 7, 8], "Осень": [9, 10, 11]}
month = int(input("Введите номер месяца: "))
if month not in range(1, 12, 1):
    print(f"Веденное значение находится за границами разрешенного диапазона значений [0 .. 12]")
else:
    if month in month_list[0]:
        month_list_index = 1
    elif month in month_list[2]:
        month_list_index = 3
    elif month in month_list[4]:
        month_list_index = 5
    elif month in month_list[6]:
        month_list_index = 7
    print(f"Результат через список: ", month_list[month_list_index])

    for key in month_dict.keys():
        for value in month_dict[key]:
            if month == value:
                print(f"Результат через словарь: ", key)
        
