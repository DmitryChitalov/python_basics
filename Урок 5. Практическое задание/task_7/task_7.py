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


profit_dict = {"average_profit": 0}
firms_dict = {}
with open("input.txt", "r", encoding="UTF-8") as f:
    data = f.readlines()
    data = [x.split() for x in data]
    data = [[x[0], x[1], int(x[2]), int(x[3]), (int(x[2]) - int(x[3]))] for x in data]
count = 0
for i in data:
    if i[-1] >= 0:
        profit_dict["average_profit"] += i[-1]
        count += 1
    firms_dict[i[0]] = i[-1]

profit_dict["average_profit"] = profit_dict["average_profit"] / count
with open("output.json", "w", encoding="UTF-8") as f:
    json.dump([firms_dict, profit_dict], f, indent=4)
