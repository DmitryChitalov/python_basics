"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""
winter = ['1', '2', '12']
spring = ['3', '4', '5']
summer = ['6', '7', '8']
autumn = ['9', '10', '11']
year_dict = {
    '1': 'winter',
    '2': 'winter',
    '3': 'spring',
    '4': 'spring',
    '5': 'spring',
    '6': 'summer',
    '7': 'summer',
    '8': 'summer',
    '9': 'autumn',
    '10': 'autumn',
    '11': 'autumn',
    '12': 'winter'
}
user_month = input(f'Введите месяц в виде целого числа от 1 до 12: ')

if user_month in winter:
    print('Результат через список: Зима')
elif user_month in spring:
    print('Результат через список: Весна')
elif user_month in autumn:
    print('Результат через список: Осень')
elif user_month in summer:
    print('Результат через список: Лето')

if year_dict.get(user_month) == 'winter':
    print('Результат через словарь: Зима')
elif year_dict.get(user_month) == 'summer':
    print('Результат через словарь: Лето')
elif year_dict.get(user_month) == 'spring':
    print('Результат через словарь: Весна')
elif year_dict.get(user_month) == 'autumn':
    print('Результат через словарь: Осень')
