list_seasons = ["summer", "autumn", "winter", "spring"]
my_dict = dict(key_1="summer", key_2="autumn", key_3="winter", key_4="spring")
month = int(input("Month number? "))
if month == 12 or month == 1 or month == 2:
    my_dict.get(2)
    print(f"This is {list_seasons[2]}, my friend")
elif month == 3 or month == 4 or month == 5:
    my_dict.get(3)
    print(f"This is {list_seasons[3]}, my friend")
elif month == 6 or month == 7 or month == 8:
    my_dict.get(0)
    print(f"This is {list_seasons[0]}, my friend")
elif month == 9 or month == 10 or month == 11:
    my_dict.get(1)
    print(f"This is {list_seasons[1]}, my friend")
else:
    print("The number is not correct")

"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""
