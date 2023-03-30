"""
Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее ​не включать.​
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка:
[{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}]
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"​firm_1":​​5000,​"​firm_2":​3​000,​​"firm_3":​​1000}​, {"​average_profit":​​2000}​]
Подсказка: использовать менеджер контекста.
"""
import json

companies_data = []

with open('7.txt') as input_data:
    companies_dict = {}
    profit_list = []

    for company_row in input_data:
        name, form, revenue, costs = company_row.split()

        profit = float(revenue) - float(costs)
        companies_dict[name] = profit

        if profit:
            profit_list.append(profit)

    companies_data.append(companies_dict)
    companies_data.append({
        "average_profit": round(sum(profit_list) / len(profit_list), 2)
    })

with open('7.json', 'w') as output_data:
    json.dump(companies_data, output_data)