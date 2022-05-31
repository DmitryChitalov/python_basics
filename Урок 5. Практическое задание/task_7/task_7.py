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

with open('firms.txt', encoding='utf-8') as f_firms:
    list_profit = []
    firms_dict = {}
    average_profit_dict = {}
    result = []
    for line in f_firms.readlines():
        name, form, revenue, costs = line.split()
        profit = int(revenue) - int(costs)
        print(f'Прибыль компании {name} составила: {profit}')
        if profit > 0:
            list_profit.append(profit)
        firms_dict[name] = profit
        average_profit = sum(map(int, list_profit)) / len(list_profit)
        average_profit_dict['average_profit'] = average_profit
    result.append(firms_dict)
    result.append(average_profit_dict)
    print(f'Средняя прибыль составила: {average_profit}')
    print(result)

with open('firms.json', 'w', encoding='utf-8') as j_obj:
    json.dump(result, j_obj)
