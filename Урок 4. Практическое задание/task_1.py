from sys import argv

"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

def get_payroll(hours, rate, reward):
    print(f"Размер заработной платы: {hours * rate + reward}")

try:
    hours_count = int(argv[1])
    rate_hour = int(argv[2])
    reward_value = int(argv[3])

    get_payroll(hours_count, rate_hour, reward_value)

except ValueError:
    print(f"Ошибка конвертации значений [{argv[1]}, {argv[2]}, {argv[3]}] в тип <int>")
