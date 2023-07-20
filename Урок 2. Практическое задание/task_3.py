"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

"""
Вариант 1
"""
print("\nВариант 1: list.\n")

month_name_lst = ["Зима", "Весна", "Лето", "Осень"]

input_month_lst = int(input("Введите номер месяца:"))

if input_month_lst == 1 or input_month_lst == 2 or input_month_lst == 12:
    print(month_name_lst[0])
if input_month_lst == 3 or input_month_lst == 4 or input_month_lst == 5:
    print(month_name_lst[1])
if input_month_lst == 6 or input_month_lst == 7 or input_month_lst == 8:
    print(month_name_lst[2])
if input_month_lst == 9 or input_month_lst == 10 or input_month_lst == 11:
    print(month_name_lst[3])
if input_month_lst <= 0 or input_month_lst >= 13:
    print("\nТакого номера месяца нет.Введите число от 1 до 12.\n")

"""
Вариант 2
"""
print("\nВариант 2: dict.\n")

season_dict = {
    "Зима": [12,1,2],
    "Весна": [3,4,5],
    "Лето": [6,7,8],
    "Осень": [9,10,11]
}

input_month_dict = int(input("Введите номер месяца:"))

for key, value in season_dict.items():
    if input_month_dict in value:
        print(key)
        break
else:
    print("\nТакого номера месяца нет.Введите число от 1 до 12.\n")
