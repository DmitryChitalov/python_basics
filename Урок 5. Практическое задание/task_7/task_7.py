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

from statistics import mean
from json import dumps


def firms_analyse():
    try:
        with open('text', 'r') as f_obj:
            res = [{}, {'average_profit': 0}]
            profits = []
            for i in f_obj:
                i = i.split()
                for el in i:
                    i[i.index(el)] = int(el) if el.isdigit() else el
                res[0][i[0]] = i[2] - i[3]
                profits.append(i[2] - i[3]) if i[2] > i[3] else ''
            res[1].update(dict(average_profit=mean(profits)))
            return True, res
    except Exception as e:
        return False, e


def create_jsonfile(obj, filename):
    try:
        with open(filename, 'w') as f_obj:
            f_obj.write(dumps(obj))
    except IOError:
        print('Warning: error input output')


if __name__ == '__main__':
    is_firms_analyse, res_obj = firms_analyse()
    if is_firms_analyse:
        create_jsonfile(res_obj, '1.json')
