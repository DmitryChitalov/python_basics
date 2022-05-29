"""
7)	Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка должна содержать данные о фирме: название, форма
собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли
ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
 а также словарь со средней прибылью. Если фирма получила убытки, также
 добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
import json

firms = {}
average_profit = {}
total_profit = 0
count_firms = 0
with open("input.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
for line in lines:
    title, form_of_ownership, revenue, costs = line.split()
    profit = int(revenue) - int(costs)
    firms[title] = profit
    if profit >= 0:
     count_firms += 1
     total_profit += profit
average_profit['average_profit'] = total_profit / count_firms

firm_list = [firms, average_profit]

with open("output.txt", "w", encoding="utf-8") as file:
    json.dump(firm_list, fp=file, ensure_ascii=False)
