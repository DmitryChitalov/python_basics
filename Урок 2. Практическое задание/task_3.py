"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

month = int(input('Введите номер месяца: '))
periods = ['Winter', 'Spring', 'Summer', 'Autumn']
print()
if month in [1, 2, 12]:
    print(f'Результат через список: {periods[0]}')
elif month in [3, 4, 5]:
    print(f'Результат через список: {periods[1]}')
elif month in [6, 7, 8]:
    print(f'Результат через список: {periods[2]}')
elif month in [9, 10, 11]:
    print(f'Результат через список: {periods[3]}')

periods_dict = {'Winter': [1, 2, 12], 'Spring': [3, 4, 5], 'Summer': [6, 7, 8], 'Autumn': [9, 10, 11]}

for k, v in periods_dict.items():
    if month in v:
        print(f'Результат через словарь: {k}')
