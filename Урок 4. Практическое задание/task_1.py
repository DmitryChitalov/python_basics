"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

def simple_calc():
    hours = float(input('Введите количество отработанных часов : '))
    rate_e = float(input('Введите суммы оплаты труда за 1 час : '))
    premium = float(input('Укажите размер премии - '))
    pay = hours * rate_e
    salary = premium + pay
    return pay + salary
print(f'Размер заработной платы составил: {simple_calc() }')