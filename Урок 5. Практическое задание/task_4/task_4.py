"""
3. Создать текстовый файл (не программно), построчно записать фамилии
сотрудников и величину их окладов (не менее 10 строк). Определить,
кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

with open('task_4_text.txt', 'r', encoding='utf-8') as salary_file:
    total_salary = 0
    workers = 0
    for line in salary_file:
        worker_salary = float(line.split()[1])
        total_salary += worker_salary
        if worker_salary < 20000:
            print(f'{line.split()[0]}')
        workers += 1
average_salary = total_salary / workers
print(f'Average salary is {average_salary}')
