"""
7)	Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о
фирме: название, форма собственности, выручка, издержки.
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
import json

profit_companies = 0
report_companies = []
with open('companies.txt', 'r', encoding='UTF-8') as file:
    text = file.read()
    file.seek(0)
    info_profit = {}
    final_profit = 0
    for row in file:
        items = row.split()
        profit = int(items[2]) - int(items[3])
        info_profit.update({items[0]: profit})
        if profit > 0:
            profit_companies += 1
            final_profit += profit
    report_companies.append(info_profit)
    report_companies.append({'average_profit': (final_profit)})
with open('companies.json', 'w', encoding='UTF-8') as file_json:
    json.dump(report_companies, file_json)
json_report = json.dumps(report_companies)
