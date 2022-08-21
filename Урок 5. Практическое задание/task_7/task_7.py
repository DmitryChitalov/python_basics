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

lst_result = []
with open("c:\Python38\\text8.txt", "r", encoding="utf-8") as my_file:
    dict_firm = {}
    dict_average = {"average_profit": 0}
    result_value = 0
    count_value = 0
    while True:
        line = my_file.readline()
        if not line:
            break
        lst_line = line.split()
        if len(lst_line) == 4:
            firm = lst_line[0].replace("\ufeff", "")
            dict_firm[firm] = float(lst_line[2]) - float(lst_line[3])
            if dict_firm[firm] > 0:
                result_value += dict_firm[firm]
                count_value += 1
    if count_value > 0:
        dict_average["average_profit"] = round(result_value / count_value, 2)
    lst_result.append(dict_firm)
    lst_result.append(dict_average)
print(lst_result)
with open("c:\Python38\\text8.json", "w") as write_file:
    json.dump(lst_result, write_file)
