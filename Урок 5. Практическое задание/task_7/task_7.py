"""
7)	Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные
о фирме:название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки,в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
import json


def average_profit(income):
    summ = 0
    count = 0
    for el in income.values():
        summ += el if el > 0 else 0
        count += 1 if el > 0 else 0
    return summ / count


def firms_income(data):
    res = {}
    for item in data:
        res[item.split()[0]] = float(item.split()[2]) - float(item.split()[3])
    return res


with open('text.txt', 'r', encoding='utf-8') as f:
    average_p = {'average_profit': None}
    income = firms_income(f.readlines())
    average_profit_value = average_p(income)
    average_p['average_profit'] = average_profit_value
    result = [income, average_p]
    with open('result.json', 'w', encoding='utf-8') as res_json:
        json.dump(result, res_json)

