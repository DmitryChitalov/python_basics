'''
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
'''
'''
def simple_calc():
    x = float(input('Введите количество отработанных часов : '))
    y = float(input('Введите суммы оплаты труда за 1 час : '))
    c = float(input('Укажите размер премии - '))
    pay = x * y
    return pay + c
print(f'Размер заработной платы составил: {simple_calc() }')
'''
#переработка 29.01.23
from sys import argv

x = float(input('Введите количество отработанных часов : '))
y = float(input('Введите сумму оплаты труда за 1 час : '))
c = float(input('Укажите размер премии: '))

script_name, productivity, hourly_rate, bonus = argv, x, y, c

print('-' * 30)
print(f'Выработка в часах: {productivity:}')
print(f'Cтавка в час: {hourly_rate:}')
print(f'Премия: {bonus:}')
try:
    print(f'Заработная плата: {float(productivity) * float(hourly_rate) + float(bonus):}')
except ValueError:
    print('Введено недопустимое значение')
print('-' * 30)