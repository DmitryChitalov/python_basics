"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""
month_num = int(input("Введите номер месяца: "))
seasons_list = ['зима', 'весна', 'лето', 'осень']
seasons_dict = {"зима" : [12, 1, 2], "весна" : [3, 4, 5], "лето" : [6, 7, 8], "осень" : [9, 10, 11]}

print("Результат через список: ", end='')

if month_num in [12, 1, 2]:
    print(seasons_list[0])
elif month_num in [3, 4, 5]:
    print(seasons_list[1])
elif month_num in [6, 7, 8]:
    print(seasons_list[2])
elif month_num in [9, 10, 11]:
    print(seasons_list[3])
else:
    print("неправильно указан номер месяца")

is_found = False
for key, val in seasons_dict.items():
    if month_num in val:
        is_found = True
        print("Результат через словарь: ", key)
        break
if not is_found:
        print("Результат через словарь: неправильно указан номер месяца")
