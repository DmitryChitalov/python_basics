"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""
from functools import reduce

with open('tex.txt', 'r', encoding='utf-8') as f:
    di = {}
    di = {x.split()[0] : float(x.split()[1]) for x in f.readlines()}
    val = [i for i in di.values() if i > 20000]
    fam = [k for k, v in di.items() if v in val]
    print('\n'.join(fam), f'средняя величена дохода - {(reduce(lambda a,b : a + b, di.values()) / len(di.values()))}',
          sep='\n\n')
