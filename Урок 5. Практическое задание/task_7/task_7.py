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

my_list = {}
my_list1 = []
my_list2 = []
my_list3 = []
with open('test.txt', 'r', encoding='utf-8') as my_file:
    for line in my_file:
        name, form, revenue, costs = line.split()
        my_profit = int(revenue) - int(costs)
        my_list[name] = my_profit
        my_list2.append(my_profit)
        if my_profit > 0:
            my_list1.append(my_profit)
    my_list3.append(my_list)
    my_list3.append({"average_profit": round(sum(my_list1) / len(my_list2), 2)})
with open('test.json', 'w+', encoding='utf-8') as my_file_out:
    json.dump(my_list3, my_file_out, ensure_ascii=False)
    my_file_out.seek(0)
    print(my_file_out.read())
