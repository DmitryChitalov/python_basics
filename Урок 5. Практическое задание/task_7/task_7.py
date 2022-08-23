"""
7)	Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать
данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также
добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
import json
result = []
with open('task_7.txt', 'r', encoding='UTF-8') as my_file:
    text = my_file.read()
    my_file.seek(0)
    prof = {}
    profits = 0
    for el in my_file:
        summ = el.split('  ')
        profit = int(summ[2]) - int(summ[3])
        if profit > 0:
            prof.update({summ[0]: profit})
            profits += profit
    result.append(prof)
    result.append({'average_profit': (profits / len(prof))})

with open('task_7.json', 'w', encoding='UTF-8') as json_file:
    json.dump(result, json_file)
json_result = json.dumps(result)
print(result)
