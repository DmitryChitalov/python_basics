"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

filename = 'employees.txt'
less_than_20k = []
total_salary = 0
num_employees = 0

with open(filename, 'r', encoding='utf-8') as file:
    for line in file.readlines():
        name, salary = line.split()
        salary = float(salary)
        total_salary += salary
        num_employees += 1
        if salary < 20000:
            less_than_20k.append(name)

avg_salary = total_salary / num_employees

print("Сотрудники с окладом менее 20 тыс.:", less_than_20k)
print("Средняя заработная плата сотрудников:", avg_salary)
