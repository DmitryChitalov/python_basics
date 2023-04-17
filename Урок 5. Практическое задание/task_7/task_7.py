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
firms_list = []
firms_dict = {}
profit_list = []
with open('firms.txt', encoding='utf-8') as f_obj:
    for line in f_obj:
        name, form, revenue, costs = line.split()
        profit = int(revenue) - int(costs)
        firms_dict[name] = profit
        if profit > 0:
            profit_list.append(profit)
firms_list.append(firms_dict)
firms_list.append({'Средняя прибыль': sum(profit_list) / len(profit_list)})
with open('firms.json', 'w') as write_f:
    json.dump(firms_list, write_f)
