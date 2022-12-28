"""
7)	Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме:
 название, форма собственности, выручка, издержки.
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
with open("test_file.txt", "r", encoding='UTF-8') as source_file:
    result_list = []
    firms_dict = {}
    lines = source_file.readlines()
    cnt = 0
    total_profit = 0
    for line in lines:
        firm_name = line.split('   ')[0]
        profit = float(line.split('   ')[2]) - float(line.split('   ')[3])
        firms_dict.update({firm_name: profit})
        total_profit = total_profit + profit
        cnt = cnt + 1
    avg_profit = round(total_profit / cnt, 2)
    result_list = [firms_dict, {'average_profit': avg_profit}]

print(result_list)
with open("firms_stats.json", "w") as result_file:
    json.dump(result_list, result_file)