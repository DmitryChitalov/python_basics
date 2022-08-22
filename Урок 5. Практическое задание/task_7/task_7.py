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

with open('text.txt', 'r+', encoding='utf-8') as f:
    statistics = []
    profit = {}
    average_profit = {}
    prof = 0
    medium_value = 0
    i = 0
    for line in f:
        name, firm, earning, damage = line.split()
        total = int(earning) - int(damage)
        if total > 0:
            prof = prof + total
            medium_value += total
            i += 1
        profit[name] = total
    statistics.append(profit)
    average_profit['Средняя прибыль'] = medium_value / i
    print(statistics)
    print(average_profit)
with open('file.json', 'a+', encoding='utf-8') as json_file:
    json.dump(statistics, json_file)
    json.dump(average_profit, json_file)


