"""
7)	Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные
 о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
 убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
 Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
import json

profit = {}
total = 0
avg = 0
i = 0


read_file = open('firms.txt', 'r')
for read_line in read_file.readlines():
    firm_name, ownership, revenue, costs = read_line.split()
    profit[firm_name] = int(revenue) - int(costs)
    if profit.setdefault(firm_name) >= 0:
        total += profit.setdefault(firm_name)
        i += 1
read_file.close()

if i != 0:
    avg = total / i
    print(f"Средняя прибыль:", avg)
else:
    print('Прибыль ТЮТЮ!')
print(f"Прибыль всех компаний: ", profit)

with open('statistic.json', 'w') as json_file:
    json.dump([profit, {"avg": avg}], json_file)
