"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""
# Решение через list
month = int(input("Введите номер месяца: "))
season = ["winter", "spring", "summer", "autumn"]
if month == 0 or month < 0:
    print("Вы ввели недопустимый номер месяца: Введите от 1 до 12")
elif month == 12 or month <= 2:
    print("Результат через список:", season[0])
elif month == 3 or month <= 5:
    print("Результат через список:", season[1])
elif month == 6 or month <= 8:
    print("Результат через список:", season[2])
elif month == 9 or month <= 11:
    print("Результат через список:", season[3])
else:
    print("Вы ввели недопустимый номер месяца: Введите от 1 до 12")

# Решение через dict
season = {1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring', 5: 'spring', 6: 'summer', 7: 'summer', 8: 'summer',
          9: 'autumn', 10: 'autumn', 11: 'autumn', 12: 'winter'}
if month in season:
    print("Результат через словарь:", season[month])
else:
    print("Вы ввели недопустимый номер месяца: Введите от 1 до 12")

