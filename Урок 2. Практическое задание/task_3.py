"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""
month_number = int(input("Введите номер месяца: "))
month_list = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август",
              "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
result_list = ["зима", "весна", "лето", "осень"]
if month_number == 12 or month_number < 3:
    print(f"Вы ввели {month_number}, это {month_list[month_number - 1]}, Результат через список: {result_list[0]}")
elif 3 <= month_number < 6:
    print(f"Вы ввели {month_number}, это {month_list[month_number - 1]}, Результат через список: {result_list[1]}")
elif 6 <= month_number < 9:
    print(f"Вы ввели {month_number}, это {month_list[month_number - 1]}, Результат через список: {result_list[2]}")
elif 9 <= month_number <= 11:
    print(f"Вы ввели {month_number}, это {month_list[month_number - 1]}, Результат через список: {result_list[3]}")

month_dict = {'Зима':  [12, 1, 2],
              'Весна': [3, 4, 5],
              'Лето':  [6, 7, 8],
              'Осень': [9, 10, 11]}

for i in month_dict.items():
    if month_number in i[1]:
        print(f'Вы ввели {month_number}, это {month_list[month_number - 1]}, Результат через словарь: {i[0]}')
