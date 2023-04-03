"""
7)	Создать вручную и заполнить несколькими строками текстовый файл, 
в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. 
Если фирма получила убытки, в расчет средней прибыли ее не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. 
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджер контекста.
"""
#!/usr/bin/env python3

import json

input_data = []
winners_data = []
data_per_business = {}
profit_calc = []
profitability_list = []
average_profit = 0
average_profit_dict = {}
happy_end = []


with open("input_file7.txt") as input_source:
    for i in input_source:
        input_data.append(i)

    for j in input_data:
        fiscal_data = j.split()
        data_per_business[fiscal_data[0]] = (int(fiscal_data[2]) - int(fiscal_data[3]))
        if int(fiscal_data[2]) > int(fiscal_data[3]):
            winners_data.append(j.strip())
    
    for k in winners_data:
        profit_calc = k.split()
        single_profit = (int(profit_calc[2]) - int(profit_calc[3]))
        profitability_list.append(single_profit)
                
    average_profit = sum(profitability_list) / len(profitability_list)

    average_profit_dict["average_profit"] = average_profit

    happy_end = [data_per_business, average_profit_dict]

json_format = json.dumps(happy_end)
print(json_format)

with open("output_file7.json", "w", encoding="UTF-8") as output_file:
    json.dump(happy_end, output_file, ensure_ascii = False, indent = 4)
