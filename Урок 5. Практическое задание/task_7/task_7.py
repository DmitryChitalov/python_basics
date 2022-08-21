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
my_f = open("task7.txt", encoding='utf-8')
res_list = []
profit_dir = {}
lusses_dir = {}
profit = 0
lusses = 0

for i in my_f.readlines():
    content = i.split()
    if int(content[2]) > int(content[3]):
        profit_dir[content[0]] = int(content[2]) - int(content[3])
        profit = profit + int(content[2]) - int(content[3])
    else:
        lusses_dir[content[0]] = int(content[2]) - int(content[3])
        lusses = lusses + int(content[2]) - int(content[3])
res_list.append(profit_dir)
res_list.append(lusses_dir)
res_list.append({"average_profit": profit / len(profit_dir)})
res_list.append({"lusses": lusses})
my_f.close()
print(res_list)
