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


# pylint: disable=invalid-name

import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('my_file.txt', "r", encoding='utf-8') as file:
    for line in file:
        name, form, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.get(name) >= 0:
            prof += profit.get(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print('средняя прибыль -', round(prof_aver, 2))
    else:
        print('Прибыль средняя - отсутсвует. Все работают в убыток')
    pr = {'average_profit': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')


with open('my_file.json', 'w', encoding='utf-8') as js_file:
    json.dump(profit, js_file)
    js_str = json.dumps(profit)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')
