"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

salary_all = open('task_4.txt', 'r', encoding='utf-8')
total_salary = 0
employ = 0
for line in salary_all:
    employ_salary = float(line.split()[1])
    total_salary += employ_salary
    if employ_salary < 20000:
        print(f'{line.split()[0]} {line.split()[1]}')
        employ += 1
print(f'Доход сотрудников в среднем составляет: {total_salary / employ}')