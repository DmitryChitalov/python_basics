"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

month_dict = {
    1: "Winter", 
    2: "Winter",
    3: "Spring",
    4: "Spring",
    5: "Spring",
    6: "Summer",
    7: "Summer",
    8: "Summer",
    9: "Autumn",
    10: "Autumn",
    11: "Autumn",
    12: "Winter"
}

month_list = ["Winter", "Winter", "Spring", "Spring", "Spring", "Summer", "Summer", "Summer", "Autumn", "Autumn", "Autumn", "Winter"]

input_month_number = input("Please, print a number in 1-12 range: ")
if str.isdigit(input_month_number):
    month_number = int(input_month_number)
    if month_number >= 1 and month_number <= 12:
        print(f"In list: season is {month_list[month_number - 1]}")
        print(f"In dict: season is {month_dict.get(month_number)}")
    else:
        print("Error: your number is not in 1-12 range")
else:
    print("Error: your number is not integer value")