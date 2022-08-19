"""
7)	Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
import json
import os


cur_dir = os.path.join('Урок 5. Практическое задание', 'task_7')
file_path_read = os.path.join(cur_dir, 'task_7_data.txt')
file_path_write = os.path.join(cur_dir, 'task_7_result.json')
result = []
with open(file_path_read, 'r', encoding='utf-8') as f:
    data = f.readlines()
    data = [el.split() for el in data]
    revenue_dict = {}
    for name, form, sales, spends in data:
        revenue_dict[name] = int(sales) - int(spends)
    profitable_vals = [el for el in revenue_dict.values() if el > 0]
    av_profit = {"average_profit": sum(profitable_vals) / len(profitable_vals)}
    result = [revenue_dict, av_profit]
    print(result)
with open(file_path_write, 'w', encoding='utf-8') as f:
    j_res = json.dumps(result)
    f.write(j_res)
