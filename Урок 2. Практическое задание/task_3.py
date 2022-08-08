"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""
months = int(input("Введите номер месяца: "))
weather_list = ["Зима", "Весна", "Лето", "Осень"]
if months in range(3, 6):
    print(f"Результат через список: {weather_list[1]}")
elif months in range(6, 9):
    print(f"Результат через список: {weather_list[2]}")
elif months in range(9, 12):
    print(f"Результат через список: {weather_list[3]}")
elif months == 1 or months == 2 or months == 12:
    print(f"Результат через список: {weather_list[0]}")
else:
    print("Нет такого месяца")

weather_dict = {"Зима" : [1, 2, 12], "Весна" : [3, 4, 5],
                "Лето" : [6, 7, 8], "Осень": [9, 10, 11]}
for key in weather_dict:
    for numbers in weather_dict[key]:
        if months == numbers:
            print(f"Результат через словарь: {key}")

