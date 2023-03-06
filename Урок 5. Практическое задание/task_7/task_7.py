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
def rent_in_line(line):
    for i in range(2, 3):
        rent = int(line[i]) - int(line[i + 1])
    return rent

good_firms = []
rent_list = []

with open('companies.txt', 'r', encoding='utf-8') as file:
    for line in file:
        rent = (rent_in_line(line.split()))
        if rent > 0:
            good_firms.append(line.split())
            rent_list.append(rent)

total = 0
for el in rent_list:
    total += el
av_rent = total / len(rent_list)
profit_dict = {'average_profit': av_rent}

firmas_list = []
for el in good_firms:
    firmas_list.append(el[0])

profit_firms = dict(zip(firmas_list, rent_list))
profit_list = [profit_firms, profit_dict]

import json

with open('profit_companines.json', 'w') as out_file:
    json.dump(profit_list, out_file)