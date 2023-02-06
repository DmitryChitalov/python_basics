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
avr_profit = 0
profit_firms = 0
loses_firm = 0
avr_dict = {}
firm_dict = {}
loses_dict = {}
with open('file1.txt', 'r', encoding='utf-8') as in_file:
    for line in in_file:
        name, form, gain, costs = line.split()
        profit = int(gain) - int(costs)
        if profit >= 0:
            avr_profit = avr_profit + profit
            profit_firms += 1
            avr_dict['Average profit w/o loses'] = round(avr_profit / profit_firms)
        else:
            loses_firm += 1
            loses_dict['Loses'] = profit
        firm_dict[name] = profit
if loses_firm > 0:
    firm_list = [firm_dict, avr_dict, loses_dict]
else:
    firm_list = [firm_dict, avr_dict]
print(firm_list)
with open('file2.json', 'w', encoding='utf-8') as out_file:
    json.dump(firm_list, out_file)
