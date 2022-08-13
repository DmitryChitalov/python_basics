"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""
list_months = ['Зима', 'Весна', 'Лето', 'Осень']
dict_months = {0: 'Зима', 1: 'Весна', 2: 'Лето', 3: 'Осень'}
user_data = int(input("Введите номер месяца: "))
if user_data == 1 or user_data == 2 or user_data == 12:
    print(list_months[0])
    print(dict_months[0])
elif user_data == 3 or user_data == 4 or user_data == 5:
    print(list_months[1])
    print(dict_months[1])
elif user_data == 6 or user_data == 7 or user_data == 8:
    print(list_months[2])
    print(dict_months[2])
elif user_data == 9 or user_data == 10 or user_data == 11:
    print(list_months[3])
    print(dict_months[3])
else:
    print("Номер указан некоректно")
