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

firm_list = []
total_profit = 0
total_count = 0

with open("firm_data.txt", "r") as f:
    for line in f:
        data = line.split()

        name = data[0]
        ownership = data[1]
        revenue = float(data[2])
        expenses = float(data[3])

        profit = revenue - expenses

        total_profit += profit

        firm_list.append({name: profit})

        if profit > 0:
            total_count += 1

average_profit = total_profit / len(firm_list)

average_dict = {"average_profit": average_profit}

firm_list.append(average_dict)

# запись списка в файл в формате json
with open("firm_list.json", "w") as f:
    json.dump(firm_list, f)

print(firm_list)
