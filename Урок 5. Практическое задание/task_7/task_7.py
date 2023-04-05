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

finance = {}
comp_finance = {}
a = [comp_finance, finance]
b = 0
calc_comp = 0

with open("nata7.txt", encoding='cp1251') as f:
    for line in f:
        name, form, salary, cost = line.split()
        margin = float(salary) - float(cost)
        if margin > 0:
            calc_comp = calc_comp + 1
            b = b + margin
            comp_finance[name] = margin
if calc_comp > 0:
    finance["average_finance"] = b / calc_comp

with open("nata7.json", "w", encoding='cp1251') as write_f:
    json.dump(a, write_f)
print(f"{comp_finance} {finance}")