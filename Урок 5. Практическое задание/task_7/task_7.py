"""
7)	Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о
фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
import json

example_list = []

summ = 0
count_comp = 0

exp_dict = {}
average_d = {}


# Функция считает среднюю прибыль по компаниям, которые работают в +
def cp_summ(take, tax):
    cp = take / tax
    cp_correct = round(cp, 2)
    return cp_correct


# Функция записывает список example_list в JSON формат в файл example.json
def save_json(e_list):
    with open('example.json', 'w') as f:
        json.dump(e_list, f)


with open('exp.txt', 'r') as file:
    for i in file:
        date = i.rstrip('\n').split()

        if int(date[2]) > int(date[3]):
            gain = int(date[2]) - int(date[3])
            summ += gain
            count_comp += 1
            exp_dict[date[0]] = gain

        else:
            gain_2 = int(date[2]) - int(date[3])
            exp_dict[date[0]] = gain_2

example_list.append(exp_dict)

average_profit = cp_summ(summ, count_comp)

average_d['average_profit'] = average_profit
example_list.append(average_d)

save_json(example_list)
