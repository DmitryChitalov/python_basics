"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

season = int(input("Введите месяц цифрой: "))
if season <= 0 or season > 12:
    print('Такого месяца не существует')
elif 2 < season < 6:
    print('Это весна')
elif 5 < season < 9:
    print('Это лето')
elif 8 < season < 12:
    print('Это осень')
else:
    print('Это зима')

season_dict = {1: "январь", 2: "февраль", 3: "март", 4: "апрель", 5: "май", 6: "июнь", 7: "июль",
               8: "август", 9: "сентябрь", 10: "октябрь", 11: "ноябрь", 12: "декабрь"}

for month in season_dict.keys():
    if season == month:
        print(f"А месяц - {season_dict[month]}")
    if season != month:
        continue
