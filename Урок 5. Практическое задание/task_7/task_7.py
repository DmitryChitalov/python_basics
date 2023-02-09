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
total_revenue = 0
count_revenue = 0
company_balance = {}
with open("file7.txt", "r", encoding='utf-8') as file_7:
    for line in file_7:
        name, type, revenue, loss = line.split()
        profit_company = int(revenue) - int(loss)
        company_balance.update({name: profit_company})
        if profit_company > 0:
            count_revenue += 1
            total_revenue += profit_company
res = [company_balance, {"average_profit": total_revenue/count_revenue}]
print(res)
with open("file7.json", "w", encoding='utf-8') as file7_json:
    json.dump(res, file7_json)
    
