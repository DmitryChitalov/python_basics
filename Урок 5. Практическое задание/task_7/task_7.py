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

all_profit = 0
firm_count = 0
average_profit = 0
firm_dict = dict()
average_profit_dict = dict()
profit = None
temp_list = []
full_name = ""

with open("task_file7.txt", encoding="utf8") as open_file:
    for line in open_file:
        temp_list = line.split()
        profit = int(temp_list[2]) - int(temp_list[3])
        firm_dict.update({' '.join([temp_list[1], temp_list[0]]): profit})
        if profit > 0:
            firm_count += 1
            all_profit += profit

average_profit_dict.update({"average_profit": all_profit / firm_count})
data = [firm_dict, average_profit_dict]
print(data)

with open("task_file7_out.json", "w") as new_file:
    json.dump(data, new_file)

