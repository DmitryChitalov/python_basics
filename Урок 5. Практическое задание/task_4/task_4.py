"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""


import json

with open('salary.json', 'r', encoding='utf-8') as in_file:
    my_dict = json.load(in_file)
    print('Сотрудники с окладом менее 20 тыс.:')
    for key in my_dict.keys():
        if my_dict[key] < 20000:
            print(key)
print(f'Средняя заработная плата = {sum(my_dict.values())/len(my_dict):.2f}')
