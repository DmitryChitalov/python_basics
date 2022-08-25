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

all_lst = []
firm_dict = {}
profit_dict = {}
profit = 0
with open('test.txt', 'w', encoding='utf-8') as my_f:
    my_text = input("Введите данные о фирме: ")

    while my_text != '':
        my_f.writelines(my_text + '\n')
        my_text = input()

with open('test.txt', 'r', encoding='utf-8') as my_f:
    for i in my_f:
        i = i.split()
        buffer = i[0]
        i.pop(0) and i.pop(0)
        value = int(i[0]) - int(i[1])
        if value > 0:
            profit += value
        firm_dict[buffer] = value
    profit_dict['average_profit'] = profit
    all_lst.append(firm_dict)
    all_lst.append(profit_dict)
with open('profit.json', 'w', encoding='utf-8') as my_f:
    json.dump(all_lst, my_f)

