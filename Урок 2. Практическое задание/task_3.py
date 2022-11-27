"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""
month = int(input("Введите номер месяца: "))

seasons = {"зима": (1, 2, 12),
           "весна": (3, 4, 5),
           "лето": (6, 7, 8),
           "осень": (9, 10, 11)}
result = "Error"
for key, values in seasons.items():
    if month in values:
        result = key
        break
print(f"Результат через словарь: {result}")

my_list = ["зима", "весна", "лето", "осень"]
if 1 <= month <= 12:
    if month == 1 or month == 2 or month == 12:
        print(f"Результат через список: {my_list[0]}")
    elif month == 3 or month == 4 or month == 5:
        print(f"Результат через список: {my_list[1]}")
    elif month == 6 or month == 7 or month == 8:
        print(f"Результат через список: {my_list[2]}")
    elif month == 9 or month == 10 or month == 11:
        print(f"Результат через список: {my_list[3]}")
    else:
        print("Результат через список: Error")
else:
    print("Результат через список: Error")

