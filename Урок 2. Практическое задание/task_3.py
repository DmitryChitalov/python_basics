"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""
us_month = int(input("1-12 >>> "))

while us_month not in range(1, 13):
    print("Такого месяца не существует")
    us_month = int(input("1-12 >>> "))

# dict
year_dict = {"winter": (1, 2, 12),
             "summer": (6, 7, 8),
             "spring": (3, 4, 5),
             "autumn": (9, 10, 11)}

for key in year_dict.keys():
    if us_month in year_dict[key]:
        print(key)

# list
year_list = ['зима', 'весна', 'лето', 'осень']

year_ind = us_month // 3 % 4
print(f"Время года: {year_list[year_ind]}")