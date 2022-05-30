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

firms = [{}, {}]
average_profit, count = 0.0, 0

with open('file_7.txt', 'r', encoding='utf-8') as file:
    line = file.readline()
    while line:
        name, firm, receipts, costs = line.split()
        receipts, costs = int(receipts), int(costs)
        profit = receipts - costs
        if profit > 0:
            average_profit += profit
            count += 1
        firms[0][name] = profit
        line = file.readline()

    if count > 0:
        average_profit = round(average_profit / count, 2)
    firms[1]['average_profit'] = average_profit

with open('file_7.json', 'w', encoding='utf-8') as write_js:
    json.dump(firms, write_js)

js_str = json.dumps(profit)
print(f'Created a json file with the following content: \n '
      f' {firms}')
