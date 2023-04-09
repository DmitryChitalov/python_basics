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
import os

path = os.path.dirname(__file__)
accounting_dict = {}
with open((os.path.join(path, 'src_file.txt')), 'r') as file_r:
    for line in file_r:
        input_list = line.split()
        accounting_dict.update({input_list[0]: (float(input_list[2]) - float(input_list[3]))})
print(accounting_dict)
profit = []
losses = []
av_profit = 0
av_losses = 0
profit_dict = {key: value for key, value in accounting_dict.items() if value > 0}
losses_dict = {key: value for key, value in accounting_dict.items() if value <= 0}
for key, value in profit_dict.items():
    av_profit = av_profit + value / len(profit_dict)
for key, value in losses_dict.items():
    av_losses = av_losses + value / len(losses_dict)
profit.append(profit_dict)
profit.append({"average_profit": av_profit})
losses.append(losses_dict)
losses.append({"average_losses": av_losses})

with open((os.path.join(path, 'result.txt')), 'a') as file_w:
    json.dump(profit, file_w, indent=2)
with open((os.path.join(path, 'result.txt')), 'a') as file_w:
    json.dump(losses, file_w, indent=2)
