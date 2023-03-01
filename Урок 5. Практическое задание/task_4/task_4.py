"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

file_name_and_path = '/Users/aleksandr_bolokhov/Desktop/GeekBrains/DevOps/Python/homeworks/python_basics/Урок 5. Практическое задание/task_4/data.txt'

my_data = []
try:
    with open(file_name_and_path, 'r', encoding='utf-8') as file:
        my_data = file.readlines()
except IOError:
    print('Что-то пошло не так!')
    
for el in my_data:
    name, salary = el.split()
    if int(salary) < 20000:
        print(name, salary)

    