"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

""" Решение задания №3 """
# Решение с использованием list
month_list = [['зима', 12, 1, 2], ['весна', 3, 4, 5], ['лето', 6, 7, 8], ['осень', 9, 10, 11]]
month_num = int(input('Введите номер месяца (1..12): '))
if month_num in range(1, 13):
    for i, el in enumerate(month_list):
        if month_num in el[1:4]:
            print(f'Введенный месяц относится к сезону {el[0]}')
            break
else:
    print('Введен неcуществующий месяц: их всего 12!')

# Решение с использованием dict
month_dict = {'Winter': [12, 1, 2],
              'Spring': [3, 4, 5],
              'Summer': [6, 7, 8],
              'Autumn': [9, 10, 11]}
month_num = int(input('Please enter # of month (1..12): '))
if month_num in range(1, 13):
    for i in month_dict.items():
        if month_num in i[1]:
            print(f'This month refers to season {i[0]}')
            break
else:
    print('Sorry, but entered value doesn`t match with month!') 
