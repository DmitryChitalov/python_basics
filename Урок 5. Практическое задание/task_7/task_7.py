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

companies = dict()
average_profit = 0

with open('companies.txt', 'r') as f:
    for line in f:
        cells = line.strip().split()
        firm = cells[0]
        form = cells[1]
        profit = int(cells[2])
        loss = int(cells[3])

        if profit > loss:
            average_profit += profit
            companies.update({firm: profit - loss})
        else:
            companies.update({firm: loss})

data = [companies, {'average_profit': average_profit}]
print(data)

with open("companies.json", "w") as write_f:
    json.dump(data, write_f)
