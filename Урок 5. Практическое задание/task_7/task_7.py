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

profit_dict = {}
losses_dict = {}
fin = 0
count = 0

with open("task_7.txt", encoding='utf-8') as f:
    for line in f:
        count += 1
        for el in line.split():
            if el.isnumeric() and fin == 0:
                fin = int(el)
            elif el.isnumeric():
                fin -= int(el)
                if fin > 0:
                    profit_dict[line.split()[0]] = fin
                    fin = 0
                else:
                    losses_dict[line.split()[0]] = fin
                    fin = 0
result = round(sum(profit_dict.values()) / (count - len(losses_dict)), 2)
result_list = [profit_dict, {'Средняя прибыль компании': result}]
with open("task_7.json", "w", encoding='utf-8') as res:
    json.dump(result_list, res, ensure_ascii=False)
print(result_list)
print(losses_dict)
