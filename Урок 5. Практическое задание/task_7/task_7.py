import json

mainlist = []
listfirm = {}
listprofit = {}
listlosses = {}
listl = []
listl2 = []
x = 0
e = 0
with open('file1.txt', 'r', encoding='utf-8') as file2:
    for el in file2:
        a, b, c, d = el.split()
        listfirm[a] = int(c) - int(d)
        e = int(c) - int(d)
        if e > 0:
            listl.append(e)
            x += 1
        elif e < 0:
            listl2.append(e)

# Создал словарь с фирмами и прибылью + дополнительные подсчеты для других словарей

y = 0
for el, el2 in enumerate(listl):
    y += int(el2)
profit = y / x
listprofit["average_profit"] = profit
# Создал словарь профита

losses = 0
for el, el2 in enumerate(listl2):
    losses += int(el2)
listlosses["losses"] = losses
# Создал словарь убытков

mainlist.append(listfirm)
mainlist.append(listprofit)
mainlist.append(listlosses)
# Занес все словари в лист

with open("file2.json", "w") as f_n:
    json.dump(mainlist, f_n)

# Я знаю что громозко и по нубски :'( Сложно дается....


"""
7)	Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о
фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со
средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
