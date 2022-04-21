"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

import json

with open('task_4.json', encoding='utf-8') as obj_j:
    dict_d = json.load(obj_j)
    print('See below Staff list with salary which is less 20000$ per year : \n ')
    for keys, values in dict_d.items():
        if values < 20000:
            print(keys)
    print(f' \n Avarage salary payments \n {sum(dict_d.values())/len(dict_d)}')
