"""
7)	Создать вручную и заполнить несколькими строками текстовый файл, в котором
каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки,
также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""

import json
profit = {}
pr = {}
PROF = 0
PROF_AVER = 0
i = 0
with open('file_7.txt', 'r') as file:
    for line in file:
        name, firm, revenue, costs = line.split()
        profit[name] = int(revenue) - int(costs)
        if profit[name] >= 0:
#            print(profit.setdefault(name))
#            print(profit[name])
            PROF = PROF + profit[name]
            i += 1
    if i != 0:
        PROF_AVER = PROF / i
        print(f'Средняя прибыль компаний - {PROF_AVER:.2f}')
    else:
        print('Все компании работают в убыток.')
    pr = {'средняя прибыль': round(PROF_AVER)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')

with open('file_7.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'Создан json-файл со следующим содержимым: \n '
          f' {js_str}')
