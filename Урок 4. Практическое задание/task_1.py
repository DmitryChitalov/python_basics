"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""
from sys import argv


def employee_salary_calculation(output_in_hours, rate_per_hour, prize):
    """ Рсчет заработной платы сотрудника
        формула расчета: (выработка в часах*ставка в час) + премия
    :param output_in_hours  - выработка в часах
    :param rate_per_hour    - ставка в час
    :param prize            - премия
    """
    return (output_in_hours * rate_per_hour) + prize


if __name__ == "__main__":
    if len(argv) != 4:
        print('Вариант запуска программы:\ntask_1.py выработка_в_часах ставка_в_час премия')
    else:
        try:
            num = [float(_) for _ in argv[1:]]
            print(
                employee_salary_calculation(
                    float(
                        argv[1]), float(
                        argv[2]), float(
                        argv[3])))
        except ValueError:
            print('Вы ввели не числовой параметр')
