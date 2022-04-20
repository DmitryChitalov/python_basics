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

sum_ptofit = 0
camp_count = 0
firm_dict = {}
profit_dict = {}
with open("HW5_task7.txt", 'r', encoding='utf-8') as f_obj:
    for line in f_obj:
        a = line.replace('\n', '')
        b = list(a.split())
        in_money = float(b[2])
        out_money = float(b[3])
        profit = in_money - out_money
        print(f"Прибыль компании {b[0]} - {profit}")
        firm_dict[b[0]] = profit
        if profit < 0:
            continue
        else:
            sum_ptofit += profit
            camp_count += 1
        profit_dict["Средняя прибыль"] = sum_ptofit / camp_count
print(firm_dict)
print(f"Средняя прибыль - {sum_ptofit / camp_count}")
print(profit_dict)
final_list = []
final_list.append(firm_dict)
final_list.append(profit_dict)

print(final_list)

with open("my_file.json", "w") as f_obj2:
    json.dump(final_list, f_obj2)
