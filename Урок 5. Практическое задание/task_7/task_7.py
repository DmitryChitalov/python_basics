"""
7)	Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о
 фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчет средней прибыли ее не включать. Далее реализовать список. Он должен содержать словарь с фирмами и их
прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в
словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
import json, io
c_dict = {}
p_dict = {}
c_list = []
i = 0
summ_profit = 0
with open("text_file7.txt", "r", encoding='utf-8') as f_obj:
    for line in f_obj:
        line_elements = line.split()
        c_cash = int(line_elements[2])
        c_expenses = int(line_elements[3])
        c_profit = c_cash - c_expenses
        c_dict[line_elements[0]] = c_profit
        if c_profit > 0 :
            summ_profit += c_profit
            i += 1
p_dict['average_profit'] = summ_profit / i
c_list.append(c_dict)
c_list.append(p_dict)
print(c_list)
with io.open('result.txt', 'w', encoding='utf-8') as r_obj:
    r_obj.write(json.dumps(c_list, ensure_ascii=False))