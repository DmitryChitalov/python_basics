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

import json
profit_dict = [{}, {'average_profit': 0}]  # {'Фирма': Прибыль/Убытки}
with open('firminfo.txt', 'r', encoding='utf-8') as firm_file:
    firm = firm_file.readline().split()
    while firm:
        profit_dict[0][firm[0]] = int(firm[2]) - int(firm[3])
        firm = firm_file.readline().split()

for el in profit_dict[0].values():
    if el > 0:
        profit_dict[1]["average_profit"] += el / len(profit_dict[0].values())


with open('firm.json', 'w', encoding='utf-8') as firm_json:
    firm_json.write(json.dumps(profit_dict, indent=4, ensure_ascii=False))
