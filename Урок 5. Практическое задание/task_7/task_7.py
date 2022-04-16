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

firms_financial_result = {}
total_positive_financial_result = 0
count_positive_financial_result = 0

with open("task7_input.csv", "r", encoding = "utf-8") as file:
    line = file.readline()
    while line != "":
        firm_info = line.split(";")
        financial_result = float(firm_info[2]) - float(firm_info[3])
        firms_financial_result[firm_info[0]] = financial_result

        if financial_result > 0:
            total_positive_financial_result += financial_result
            count_positive_financial_result += 1

        line = file.readline()


result_lst = [firms_financial_result, { "average_profit": round(total_positive_financial_result / count_positive_financial_result, 3) }]
json_lst = json.dumps(result_lst, indent = 4)

with open("task7_output.json", "w", encoding = "utf-8") as file:
    file.write(json_lst)