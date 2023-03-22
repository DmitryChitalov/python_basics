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


def money(line):
    for i in range(2, 3):
        profit = int(line[i]) - int(line[i + 1])
    return profit


all_firms = []
profit_list = []
all_firms_profit = []
with open('firms_info.txt', 'r', encoding='utf-8') as file:
    for line in file:
        firm_balance = (money(line.split()))
        all_firms.append(line.split())
        all_firms_profit.append(firm_balance)
        if firm_balance > 0:
            profit_list.append(firm_balance)


total = 0
for el in profit_list:
    if el > 0:
        total += el

av_profit = total / len(profit_list)
profit_dict = {'Average_profit': av_profit}


firms_list = []
for el in all_firms:
    firms_list.append(el[0])


firms_profit = dict(zip(firms_list, all_firms_profit))
firms_money = [firms_profit, profit_dict]
print(firms_money)

with open('profit_firms.json', 'w', encoding='utf-8') as out_file:
    json.dump(firms_money, out_file)
