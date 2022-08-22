"""
7)	Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка
должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь
со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
import json

file_name = "file.txt"
json_file_name = "file.json"

comp_dict = {}
avg_profit = 0
comp_num = 0

with open(file_name) as in_file:
    for s in in_file:
        s_args = list(s.split(" "))
        comp_name = s_args[0]
        comp_form = s_args[1]
        try:
            comp_income = int(s_args[2])
            comp_spends = int(s_args[3])
        except ValueError:
            print(f"Ошибка в строке компании {comp_form} \"{comp_name}\"")
            comp_income = 0
            comp_spends = 0
            #exit(1)
        comp_balance = comp_income - comp_spends
        if comp_balance > 0:
            avg_profit += comp_balance
            comp_num += 1
        comp_dict.update({comp_name: comp_balance})
if comp_num > 0:
    avg_profit = avg_profit / comp_num
avg_profit_dict = {"average_profit": avg_profit}
print("Список компаний:", comp_dict)
print("Средняя прибыль: ", avg_profit_dict)

with open(json_file_name, "w") as f_n:
    json.dump(comp_dict, f_n)
    json.dump(avg_profit_dict, f_n)
