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
result_list = []
try:
    with open("source.txt") as f_obj:
        temp_list = [line.split() for line in f_obj if len(line) > 1]
        firms_dict = {el[0]:(int(el[2]) - int(el[3])) for el in temp_list}
except IOError:
    print("проблема с открытием файла. возможно его нет")
firms_with_profit = 0
total_profit = 0
for el in firms_dict:
    if firms_dict[el] > 0:
        total_profit += firms_dict[el]
        firms_with_profit += 1

result_list = [firms_dict, {"average_profit": total_profit/firms_with_profit}]
print(result_list)
with open("result.json", "w") as write_f_obj:
    json.dump(result_list, write_f_obj)
