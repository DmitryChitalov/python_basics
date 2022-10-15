"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""
user_month = int(input('Введите месяц в виде целого числа от 1 до 12: '))
seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
seasons_dict = {1 : 'Зима', 2 : 'Весна', 3 : 'Лето', 4 : 'Осень'}
if user_month ==1 or user_month == 12 or user_month == 2:
    print(f'Результат через словарь: {seasons_dict.get(1)}')
    print(f'Результат через список: {seasons_list[0]}')
elif user_month == 3 or user_month == 4 or user_month ==5:
    print(f'Результат через словарь: {seasons_dict.get(2)}')
    print(f'Результат через список: {seasons_list[1]}')
elif user_month == 6 or user_month == 7 or user_month == 8:
    print(f'Результат через словарь: {seasons_dict.get(3)}')
    print(f'Результат через список: {seasons_list[2]}')
elif user_month == 9 or user_month == 10 or user_month == 11:
    print(f'Результат через словарь: {seasons_dict.get(4)}')
    print(f'Результат через список: {seasons_list[3]}')
else:
    exit(0)
