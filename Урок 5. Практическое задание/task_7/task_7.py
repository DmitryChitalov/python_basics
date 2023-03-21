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
profit = {}
pr = {}
total_profit = 0
avg_profit = 0
q_firms = 0
with open('firms.txt', 'r', encoding='utf-8') as file:
    for line in file:
        name, form_ownership, earnings, costs = line.split()
        profit[name] = int(earnings) - int(costs)
        if profit.setdefault(name) >= 0:
            total_profit += profit.setdefault(name)
            q_firms += 1
    if q_firms != 0:
        avg_profit = total_profit / q_firms
        print(f'Средняя прибыль - {avg_profit:.2f}')
    else:
        print('Прибыль отсутсвует. Все работают в убыток')
    profit.update({'средняя прибыль': round(avg_profit)})
    print(f'Прибыль каждой компании - {profit}')

with open('avg_profit_firms.json', 'w') as write_js:
    json.dump(profit, write_js)
