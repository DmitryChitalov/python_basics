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

sum_of_profit = 0
firms_dict = dict()
profit_counter = 0
list_firms = list()
with open("file_7.txt", "r", encoding='utf-8') as f_obj:
    while True:
        line = list(f_obj.readline().split())
        if not line:
            break
        if int(line[2]) > int(line[3]):
            sum_of_profit += int(line[2]) - int(line[3])
            profit_counter += 1
        firms_dict.update({line[0]: int(line[2]) - int(line[3])})
list_firms.append(firms_dict)
list_firms.append(dict(average_profit=sum_of_profit / profit_counter))
print(list_firms)
with open("file_7_out.json", "w", encoding='utf-8') as f_obj:
    json.dump(list_firms, f_obj)
