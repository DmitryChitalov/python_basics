"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!

Process finished with exit code 0

Пример:
Введите первое число: 10
Введите второе число: 10
1.0

Process finished with exit code 0
"""

def division(num_1, num_2):
    try:
        return num_1 / num_2
    except ZeroDivisionError:
        return "куда ты делишь?"
num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))
print(division(num_1, num_2))

#Task_2
def personality(name, sname, b_date, city, email, ph_numb):
    print(f'{name} {sname}, {b_date} года рождения, проживающий в городе {city}. Электронная почта: {email}, телефон: {ph_numb}.')
personality(name = 'Глеб', sname = 'Жиглов', b_date = '1953', city = 'Москва', email = 'g_zhi@ya.ru', ph_numb = '88005553535')
