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


avg_profit = dict()
with open('file.txt', 'r', encoding='utf-8') as my_file:
    total_sum = 0
    counter = 0
    firms = dict()
    for i in my_file:
        if (int(i.split()[2]) - int(i.split()[3])) > 0:
            total_sum += (int(i.split()[2]) - int(i.split()[3]))
            counter += 1
        firms[i.split()[0]] = (int(i.split()[2]) - int(i.split()[3]))
    avg_profit['average_profit'] = total_sum / counter

with open('output.json', 'w', encoding='utf-8') as ouf:
    json.dump([firms, avg_profit], ouf, indent=4)
