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

fin = []
profit = {}
pr_avr = {}
prof = 0
i = 0
try:
    with open('t7.txt', 'r', encoding='utf-8') as file:
        for line in file:
            name, firm, rev, cost = line.split()
            diff = round(float(rev) - float(cost), 2)
            profit[name] = diff
            if diff > 0:
                prof = prof + diff
                i += 1
        fin.append(profit)
        if i > 0:
            pr_avr["Средняя прибыль"] = round(prof / i, 2)
            fin.append(pr_avr)
        else:
            print('Все компании работают в убыток')
except FileNotFoundError:
    print("Файл не найден!")

with open('t7.json', 'w+', encoding='utf-8') as json_file:
    json.dump(fin, json_file, ensure_ascii=False)
    json_file.seek(0)
    print(f"json файл: ", json_file.read())
