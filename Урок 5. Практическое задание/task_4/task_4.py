"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

total = 0.0
counts = 0

with open('salaries.txt', 'r', encoding='utf-8') as f_sal:
    for line in f_sal:
        salary = float(line.split(' ')[1])
        person = line.split(' ')[0]
        if salary < 20000:
            print(f'Зарплата менее 20000: {line}')
        total += salary
        counts += 1

print(f'Средняя зарплата: {total / counts:.2f}')
