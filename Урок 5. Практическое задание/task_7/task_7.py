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

import json as js

company_dict = dict()
avearge_dict = dict()
sum = 0
result_list = []
#Lines = {"firm_1   ООО   10000   5000"}
with open('data.txt') as file1:
    for line in Lines:
        company_dict[line.split()[0]] = int(line.split()[2]) - \
                                 int(line.split()[3])
result_list.append(company_dict)
for value in company_dict.values():
    sum += value
avearge_dict['average_profit'] = sum / len(company_dict)
result_list.append(avearge_dict)

print(result_list)

with open('result.json', 'w') as file2:
    js.dump(result_list, file2)
