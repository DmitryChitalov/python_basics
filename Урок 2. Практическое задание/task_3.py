"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

s_list = ['зима', 'весна', 'лето', 'осень']
s_dict = {0: 'зима', 1: 'весна', 2: 'лето', 3: 'осень'}
month = int(input("Введите номер месяца: "))
if month > 12 or month < 1:
    exit('Упс...')
i = month // 3
if i == 4:
    i = 0

# print(f"debug: {i}")
print(f"Результат через список: {s_list[i]}")
print(f"Результат через словарь: {s_dict.get(i)}")
