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

with open("file.txt") as f_obj:
    list_fo_lines = [line.replace('\n', '').split() for line in f_obj]
    dict_of_firm_profit = {str(line[0]): (int(line[2]) - int(line[3])) for line in list_fo_lines}
    temp = [abs(int(line[2]) - int(line[3])) for line in list_fo_lines]
    dict_of_average_profit = {'average_profit': round((sum(temp) / len(temp)), 2)}
    end_point = [dict_of_firm_profit, dict_of_average_profit]
print(end_point)

with open("file.json", "w") as write_f:
    json.dump(end_point, write_f, ensure_ascii=False)
