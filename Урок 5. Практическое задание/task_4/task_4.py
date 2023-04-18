"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""
with open('task_4.txt') as read_file:
    f_average_salary = 0
    all_read_lines = read_file.readlines()
    for line in all_read_lines:
        s_name, salary = line.split()
        salary = float(salary)
        f_average_salary += salary
        if salary < 20000:
            print(f'\t{s_name} {salary}')
    if len(all_read_lines) > 0:
        f_average_salary /= len(all_read_lines)
        print(f'\tСредняя зарплата: {f_average_salary:.2f}\n')