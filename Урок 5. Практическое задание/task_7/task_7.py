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


def analyse():
    try:
        with open('firm.txt', 'r', encoding='utf-8') as string_obj:
            result = [{}, {'average_profit': 0}]
            profits = []
            for i in string_obj:
                i = i.split()
                for el in i:
                    i[i.index(el)] = int(el) if el.isdigit() else el
                result[0][i[0]] = i[2] - i[3]
                profits.append(i[2] - i[3]) if i[2] > i[3] else ''
            result[1].update(dict(average_profit=mean(profits)))
            return result
    except Exception as e:
        return False, e


if __name__ == '__main__':
    try:
        result_analyse = analyse()
        with open('firm.json', 'w', encoding='utf-8') as obj:
            obj.write(dumps(result_analyse, ensure_ascii=False))
    except IOError:
        print('Ошибка!')
