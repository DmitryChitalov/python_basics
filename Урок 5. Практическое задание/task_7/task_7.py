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
from functools import reduce
import json


with open('Урок 5. Практическое задание/task_7/task_7.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()
    firms_income = {}
    average_profit = {'average_profit': None}
    for item in data:
        firms_income[item.split()[0]] = float(item.split()[2]) - float(item.split()[3])
    average_profit_value = reduce(lambda a, b: float(a) + float(b), firms_income.values()) / len(firms_income.values())
    average_profit['average_profit'] = average_profit_value
    result = [firms_income, average_profit]
    with open('Урок 5. Практическое задание/task_7/result.json', 'w', encoding='utf-8') as res_json:
        json.dump(result, res_json)