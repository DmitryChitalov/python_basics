__author__ = 'AndreiM'
__version__ = "1.0 18.04.2023"
print("\n task_7 \n -------- \n")

"""
7)	Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""

import json

filename = 'text_7.txt'
'''
Brooms ПАО 2500000 500000
Tandoor АО 1245000 1880000
Honey-cake ЗАО 5250000 455000
Matrioshka OOO 4770000 511000
Сказка ИП 10500000 5000000
'''

filename_js = 'text_71.json'

profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0

try:
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            name, firm, earning, damage = line.split()
            profit[name] = float(earning) - float(damage)
            if profit.setdefault(name) >= 0:
                prof = prof + profit.setdefault(name)
                i += 1
        if i != 0:
            prof_aver = prof / i
            print(f'  Прибыль средняя - {prof_aver:.2f}')
        else:
            print(f'  Прибыль средняя - отсутсвует. Все работают в убыток\n')
        pr = {'  средняя прибыль': round(prof_aver)}
        profit.update(pr)
        print(f'  Прибыль каждой компании - {profit}')

    with open(filename_js, 'w+', encoding='utf-8') as write_js:
        json.dump(profit, write_js)

        js_str = json.dumps(profit)
        print(f'  Был создан файл {filename_js} со следующим содержимым \n  {js_str}')

except FileNotFoundError:
    print(f'Error. Невозможно создать или открыть файл')