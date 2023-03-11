"""
3) Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

with open('file_for_task.txt', 'r', encoding='utf-8') as f_obj:
    salary_under_20 = []
    workers = 0
    total_salaries = 0
    avg_salary = 0

    for line in f_obj:
        workers += 1
        last_name, salary = line.split()

        if float(salary) < 20000.00:
            salary_under_20.append(last_name)

        total_salaries += float(salary)

    avg_salary = total_salaries / workers

print(f'Оклад меньше 20 тысяч у сотрудников: {", ".join(salary_under_20)}.')
print(f'Средний оклад на предприятии: {avg_salary:.2f}')
