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
firms_profit = {}
avg_profit = {}
data = [firms_profit, avg_profit]
avg_sum_profit = 0
avg_firm_count = 0

with open("task_7.txt", encoding='utf-8') as f:
    for line in f:
        name, form, incomes, expenses = line.split()
        profit = float(incomes) - float(expenses)
        if profit > 0:
            avg_firm_count += 1
            avg_sum_profit += profit
        firms_profit[name] = abs(profit)
    print(firms_profit)
if avg_firm_count > 0:
    avg_profit["average_profit"] = avg_sum_profit / avg_firm_count

with open("task_7.json", "w", encoding='utf-8') as write_f:
    json.dump(data, write_f)
print(f"{firms_profit} {avg_profit}")
