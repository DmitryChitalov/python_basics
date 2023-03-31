"""
7)	Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о
фирме: название, форма собственности, выручка, издержки.

Пример строки файла: firm_1   ООО   10000   5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчет средней прибыли ее не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
import json

total_profit = 0
firm_cnt = 0
average_profit = 0
firm_dict = dict()
av_prof_dict = dict()
prof = None
tmp_list = []
full_name = ""

with open("pnl_results.txt", encoding="utf8") as f_obj:
    for line in f_obj:
        tmp_list = line.split()
        prof = int(tmp_list[2]) - int(tmp_list[3])
        firm_dict.update({' '.join([tmp_list[1], tmp_list[0]]): prof})
        if prof > 0:
            firm_cnt += 1
            total_profit += prof

av_prof_dict.update({"average_profit": total_profit / firm_cnt})
data = [firm_dict, av_prof_dict]
print(data)

with open("json_dmp.json", "w") as write_f:
    json.dump(data, write_f)
