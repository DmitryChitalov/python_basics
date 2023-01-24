"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""


from sys import argv

script_name, hours_worked, hourly_rate, bonus = argv


def calc_salary(hours_worked, hourly_rate, bonus):
    try:
        print(f'Отработано:  {hours_worked}\nПочасовая ставка: {hourly_rate}\nПремия: {bonus}')
        print(f'Итого ЗП:  {float(hours_worked) * float(hourly_rate) + float(bonus)}')
    except ValueError:
        print("Некорректный ввод. Повторите.")
        exit()


calc_salary(hours_worked, hourly_rate, bonus)