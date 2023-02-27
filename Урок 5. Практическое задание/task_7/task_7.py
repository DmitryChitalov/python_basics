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
report = []
with open('07.txt', 'r', encoding='UTF-8') as my_fl:
    text = my_fl.read()
    my_fl.seek(0)
    profits = {}
    profit_sum = 0
    for row in my_fl:
        items = row.split(' ')
        profit = int(items[2]) - int(items[3])
        if profit > 0:
            profits.update({items[0]: profit})
            profit_sum += profit
    report.append(profits)
    report.append({'Средняя прибыль': (profit_sum / len(profits))})
with open('07.json', 'w', encoding='UTF-8') as json_fl:
    json.dump(report, json_fl, ensure_ascii=False)
json_report = json.dumps(report, ensure_ascii=False)
print(f"Исходный файл:\n{text}")
print(f"Словарь с фирмами и их прибылями:\n{report}\n")
print(f"json-файл:\n{json_report}")
