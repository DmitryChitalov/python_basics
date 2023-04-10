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

import re
import json

company_dict = {}
company_profit = 0
sum_profit = 0

# читаем файл по строкам
with open("list.txt", encoding="utf-8") as f_obj:
    for line in f_obj:
        val = list(map(int, re.findall("\d+", line)))  # получаем выручку и издержки
        key = line.split(" ")[0]  # название компании
        profit = val[1] - val[2]  # есть ли профит
        if profit > 0:
            sum_profit += profit  # общая прибыль
            company_profit += 1  # считаем прибыльние компании
            company_dict[key] = profit  # добавляем компанию и сумму прибыли в словарь
            print(f"Компания {key} получила прибыль в размере = {profit}")
        else:
            company_dict[key] = profit  # если нет прибыли, то все-равно добавляем её в словарь
            print(f"Компания {key} получила убытки в размере = {profit}")
print(f"Средняя прибыль компаний составила = {sum_profit / company_profit}")

company_average_dict = {"average_profit": sum_profit / company_profit}  # создаем словарь средней прибыли
list_dict = [company_dict, company_average_dict]  # создаем список словарей
print(f"итоговый список: {list_dict}")

# Создаём json файл и записываем в него информацию из списка
with open("result.json", "w") as json_file:
    json.dump(list_dict, json_file, ensure_ascii=False)

with open("result.json") as json_file:
    print(f"Содержимое файла json: {json.load(json_file)}")
