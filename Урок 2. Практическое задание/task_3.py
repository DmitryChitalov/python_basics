"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""
winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

season_by_month = {
    '1': 'Зима',
    '2': 'Зима',
    '3': 'Весна',
    '4': 'Весна',
    '5': 'Весна',
    '6': 'Лето',
    '7': 'Лето',
    '8': 'Лето',
    '9': 'Осень',
    '10': 'Осень',
    '11': 'Осень',
    '12': 'Зима',
}

user_month = input('Введите номер месяца: ')

if int(user_month) in winter:
    print('Результат через список: Зима')
elif int(user_month) in spring:
    print('Результат через список: Весна')
elif int(user_month) in summer:
    print('Результат через список: Лето')
else:
    print('Результат через список: Осень')

print(f'Результат через словарь: {season_by_month[user_month]}')