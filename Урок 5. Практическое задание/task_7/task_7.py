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

with open('dz_7.txt', 'r', encoding='utf-8') as file:
    statistics = []
    profit = {}
    average_profit = {}
    av = 0
    prof = 0
    for line in file:
        firm, earning, damage = line.split()
        total = int(earning) - int(damage)
        if total >= 0:
            average_profit[firm] = total
            statistics.append(average_profit)
        else:
            profit[firm] = total
            statistics.append(profit)
print(statistics)
with open('file.json', 'a+', encoding='utf-8') as json_file:
    json.dump(statistics, json_file)

    #сыровато не успел доделать
