"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

from statistics import mean

workers = open("file4.txt", 'r', encoding='utf-8')
salaries = []
for worker in workers:
    last_name, salary = worker.split()
    salary = float(salary)
    if salary < 20_000:
        print(last_name)
    salaries.append(salary)
print(mean(salaries))