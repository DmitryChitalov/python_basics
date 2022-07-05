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

dic_firms_up = {} #Словарь прибыльных фирм
dic_firms_down = {} #Словарь не прибыльных фирм
profit_sum = [] #Список прибыли прибльных фирм
count = 0
dic_average_profit = {} #Словарь средней прибыли

with open("file7.txt", encoding='utf-8') as file:
    for line in file:
        name, tip, revenue, coast = line.split()
        profit = int(revenue) - int(coast)
#        print(f"{name} - {profit}")
        if profit > 0:
            dic_firms_up[name] = profit
            count += 1
            profit_sum.append(profit)
        else:
            dic_firms_down[name] = profit
dic_average_profit['average_profit'] = int(sum(profit_sum) / count)
print(f"Всего {count} фирмы в +: {dic_firms_up}")
print(f"Фирмы в -: {dic_firms_down}")
print(dic_average_profit)
base = [dic_firms_up, dic_average_profit, dic_firms_down]

"""Полученый результат загоняю в json файл"""
import json
with open("file7_2.json", "w", encoding='utf-8') as file_json:
    json.dump(base, file_json, ensure_ascii=False)



