"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

from chardet import detect
import json

with open('file.json', 'rb') as file:
    CONTENT = file.read()
ENCODING = detect(CONTENT)['encoding']

with open('file.json', 'r', encoding=ENCODING) as my_file:
    my_dic = json.load(my_file)
    print('Сотрудники, зарабатывающие меньше  20000 в год:')
    for a, b in my_dic.items():
        if b < 20000:
            print(f'{a} : {b}')
    print(f'Средняя заработная плата = {sum(my_dic.values()) / len(my_dic)} ')
