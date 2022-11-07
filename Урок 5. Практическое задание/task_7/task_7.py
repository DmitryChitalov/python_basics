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

result_dict = [{}, {"average_profit": 0.0}, {}]

try:
    with open("firms.data", encoding="utf-8") as f_obj:
        for f_line in f_obj:
            l_parts = f_line.split("  ")

            firm_name = l_parts[0]
            income = float(l_parts[2])
            expense = float(l_parts[3])
            revenue = income - expense

            if revenue > 0:
                result_dict[0][firm_name] = revenue
            elif revenue < 0:
                result_dict[2][firm_name] = revenue

except IOError:
    print("Ошибка!")


profit_count = len(result_dict[0])
if profit_count > 0:
    result_dict[1]["average_profit"] = sum(result_dict[0].values()) / profit_count

print(f"Список:\n{result_dict}")

with open("firms.json", "w+", encoding="utf-8") as write_f:
    json.dump(result_dict, write_f)
    write_f.seek(0)
    print(f"Сохраненный файл:\n {write_f.read()}")

with open("firms.json", encoding="utf-8") as read_f:
    data = json.load(read_f)
    print(f"json из:\n {data}")
