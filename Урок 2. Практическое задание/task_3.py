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
fall = [9, 10, 11]

number_of_mounth = int(input('Введите номер месяца: '))

if number_of_mounth in winter:
    print('Зима')
if number_of_mounth in spring:
    print('Весна')
if number_of_mounth in summer:
    print('Лето')
if number_of_mounth in fall:
    print('Осень')

