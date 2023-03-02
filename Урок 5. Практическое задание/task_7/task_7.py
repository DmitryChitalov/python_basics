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


def profit(revenue, costs):
    profit = int(revenue) - int(costs)
    return profit


firm_list = []
firm_dict = {}
avg_dict = {}
amount_profit = 0

with open('firm.txt', 'r', encoding='utf-8') as firms:
    for firm in firms:
        firm = firm.split()
        firm_dict[firm[0]] = profit(firm[2], firm[3])
    firm_list.append(firm_dict)

for profit in firm_dict.values():
    amount_profit += int(profit)

avg_profit = amount_profit / len(firm_dict.values())
avg_dict['average_profit'] = avg_profit
firm_list.append(avg_dict)

with open('firm.json', 'w') as firms_json:
    json.dump(firm_list, firms_json)
