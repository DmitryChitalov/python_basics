"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""
import sys

working_hours, hourly_rate, award = sys.argv[1:]


def calculation_salary(hours, rate, award_in_percent) -> float:
    try:
        result = float(hours) * float(rate) * float(award_in_percent)
    except ValueError:
        print('Вводите корректные данные, пожалуйста! Любые типы, за исключением float и int - недопустимы!')

    return result if 'result' in locals() else exit()


def print_salary():
    salary = calculation_salary(working_hours, hourly_rate, award)
    print(f'Заработная плата исходя из введенных данных составляет {salary}')


print_salary()
