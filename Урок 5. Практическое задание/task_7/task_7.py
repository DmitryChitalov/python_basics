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

file_info = []
with open('test_7.txt', "r", encoding='utf-8') as file_from:
    with open('test_7.json', 'w', encoding='utf-8') as file_json:
        company = {}
        profit_info = []
        lines = file_from.readlines()
        for line in lines:
            line = line.split(' ')
            name = line[0]
            company[name] = round(float(line[2]) - float(line[3]), 2)
            if company[name] > 0:
                profit_info.append(company[name])
        file_info.append(company)
        file_info.append({"average_profit": round(sum(profit_info) / len(profit_info), 2)})
        json.dump(file_info, file_json)
