"""
7)	Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""

import json


def get_firm(some_str):
    words = []
    word = ""
    i = 0
    while i != len(some_str):
        if some_str[i] != " ":
            word += some_str[i]
        elif word != "":
            words.append(word)
            word = ""
        i += 1
    if word != "":
        words.append(word)
    return {words[0]: float(words[2]) - float(words[3])}


def merge_dicts(dict1, dict2):
    res = dict1.copy()
    res.update(dict2)
    return res


input_file = open('inputtextfile.txt', 'r')

firm_dict = {}
for line in input_file:
    firm_dict = merge_dicts(firm_dict, get_firm(line))

average_profit = 0
counter = 0
for el in firm_dict:
    if firm_dict[el] >= 0:
        average_profit += firm_dict[el]
        counter += 1

average_profit = average_profit / counter

result_list = [firm_dict, {"average_profit": average_profit}]

with open('outputtextfile.json', 'w') as outfile:
    json.dump(result_list, outfile)
