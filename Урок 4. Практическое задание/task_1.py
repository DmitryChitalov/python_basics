"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

import argparse

def calculate_salary(hours_worked, hourly_rate, bonus):
    """Рассчитываем заработную плату сотрудника на основе отработанных часов, почасовой ставки и бонуса."""
    salary = (hours_worked * hourly_rate) + bonus
    return salary

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Рассчитываем заработную плату сотрудника.')
    parser.add_argument('hours_worked', type=float, help='Часы, отработанные сотрудником.')
    parser.add_argument('hourly_rate', type=float, help='Почасовая ставка сотрудника.')
    parser.add_argument('bonus', type=float, help='Сумма бонуса для сотрудника.')
    args = parser.parse_args()

    salary = calculate_salary(args.hours_worked, args.hourly_rate, args.bonus)
    print(f"Заработная плата работника составляет{salary}.")
