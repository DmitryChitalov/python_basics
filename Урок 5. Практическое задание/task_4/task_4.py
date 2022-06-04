"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""
from functools import reduce


with open('Урок 5. Практическое задание/task_4/task_4.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()
    data_dict = {el.split()[0]: el.split()[1] for el in data}
    print('--------------------')
    print('Оклад менее 20 тыс. имеют:')
    for item in data_dict:
        if int(data_dict[item]) < 20000:
            print('-', item)
    print('--------------------')
    average = reduce(lambda a, b: int(a) + int(b), data_dict.values()) / len(data_dict.values())
    print(f'Cредняя величина дохода: {average}')