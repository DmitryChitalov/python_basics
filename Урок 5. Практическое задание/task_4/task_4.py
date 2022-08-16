"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""
average_salary = 0
processed_data = []
less_than_20 = []
with open('task_4_data.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()
    for el in data:
        surname, salary = el.split(' ')
        salary = float(salary)
        average_salary += salary
        processed_data.append([surname, salary])
        if salary < 20000.0:
            less_than_20.append([surname, salary])
    average_salary = average_salary / len(processed_data)
    print('Фамилии сотрудников с окладом меньше 20 000: ')
    print(less_than_20)
    print(f'Средняя величина дохода сотрудников: {average_salary}')
