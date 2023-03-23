"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

import sys


MINIMAL_SALARY = 20000
FILENAME = "task4.txt"


if __name__ == "__main__":
    try:
        with open(FILENAME, encoding='utf-8') as fh:
            employees = fh.readlines()
    except IOError as e:
        print(e)
        sys.exit(1)

    summ_salary = 0

    for employee in employees:
        name, salary = employee.split()

        try:
            salary = float(salary)
        except ValueError:
            continue

        summ_salary += salary
        if salary < MINIMAL_SALARY:
            print(name)

    print('Седний оклад сотрудников: ', round(summ_salary / len(employees), 2))
