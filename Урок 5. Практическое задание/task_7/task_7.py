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

# Читаем файл и вычисляем прибыль каждой компании
profits = {}
total_profit = 0
num_profitable_companies = 0
with open("companies.txt", "r", encoding='utf-8') as f:
    for line in f:
        data = line.split()
        name, form, revenue, costs = data
        profit = int(revenue) - int(costs)
        if profit > 0:
            profits[name] = profit
            total_profit += profit
            num_profitable_companies += 1
        else:
            profits[name] = profit

# Вычисляем среднюю прибыль
if num_profitable_companies > 0:
    avg_profit = total_profit / num_profitable_companies
else:
    avg_profit = 0


# Создаем список и записываем его в файл в формате JSON
result = [profits, {"average_profit": avg_profit}]
with open("companies.json", "w") as file:
    json.dump(result, file)
