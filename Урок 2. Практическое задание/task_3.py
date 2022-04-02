"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

month_list = [
    "winter",
    "winter",
    "spring",
    "spring",
    "spring",
    "summer",
    "summer",
    "summer",
    "autumn",
    "autumn",
    "autumn",
    "winter"
]

month_dict = {
    3: "spring",
    4: "spring",
    5: "spring", 
    6: "summer",
    7: "summer",
    8: "summer",
    9: "autumn",
    10: "autumn",
    11: "autumn",
    12:"winter",
    1: "winter",
    2: "winter"
}

month_code = int(input("Enter month: "))
print(f"From list it's month is: {month_list[month_code - 1]}")
print(f"From dict it's month is: {month_dict[month_code]}")
