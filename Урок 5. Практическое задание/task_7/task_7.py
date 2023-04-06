"""
7)	Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме: 
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, 
а также среднюю прибыль. 
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, 
а также словарь со средней прибылью. Если фирма получила убытки, 
акже добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, 
{“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
import json

total_profit = 0
count_firms = 0
dict_profit = {} #прибыль
dict_firms_with_profit = {} # фирмы с прибылью
new_list = [dict_firms_with_profit, dict_profit]

with open("input_ex7.txt", "r") as my_f:
    for string in my_f:
        my_list = list(string.split())
        profit = float(my_list[2]) - float(my_list[3])
        if profit > 0:
            count_firms += 1
            total_profit += profit
        dict_firms_with_profit[my_list[0]] = profit
if count_firms > 0:
    dict_profit["average_profit"] = total_profit / count_firms
print(f"{dict_firms_with_profit}, {dict_profit}")

with open("output_ex7.json", "w") as new_f:
    json.dump(new_list, new_f)





