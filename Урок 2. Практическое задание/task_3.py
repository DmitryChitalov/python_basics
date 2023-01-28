"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

# Решение через dict
seasons_dict = {1 : 'Зима', 2 : 'Весна', 3 : 'Лето', 4 : 'Осень'}
month = int(input("Введите месяц в виде целого числа от 1 до 12: "))
if month ==12 or month == 1 or month == 2:
        print(seasons_dict.get(1))
elif month == 3 or month == 4 or month ==5:
    print(seasons_dict.get(2))
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3))
elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(4))
else:
        print("Такого месяца не существует. Попробуйте заново.")


# Решение через list
month = int(input("Введите месяц в виде целого числа от 1 до 12 : "))
list = ["Зима", "Весна", "Лето", "Осень"]
while True:
    if month > 12 or month <= 0 :
        print(f"\tINCORRECT ID!!! \n\tPlease use number range from 1 to 12 only!")
        month = int(input("Введите месяц в виде целого числа от 1 до 12 : "))
        continue
    list = ["Зима", "Весна", "Лето", "Осень"]
    if month == 12 or (month >= 1 and month < 3):
        print(f"\tРезультат {month}  : '{list[0]}'")
        break
    elif month >= 3 and month < 6:
        print(f"\tРезультат {month} : '{list[1]}'")
        break
    elif month >= 6 and month < 9:
        print(f"\tРезультат {month} : '{list[2]}'")
        break
    elif month >= 9 and month < 12:
        print(f"\tРезультат {month} : '{list[3]}'")
        break