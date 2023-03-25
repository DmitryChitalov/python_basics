"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

"""
import sys

min_salary = 20000
my_file = "text_4.txt"

try:
    with open(my_file, 'r', encoding='utf-8') as fh:
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
    if salary < min_salary:
        print(name)

print('Средний оклад: ', round(summ_salary / len(employees), 2))
