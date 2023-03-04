import json

"""
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна
содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""


def calculate_profit(src_file, dst_file):
    res = []
    res_dict = {}
    positive_profit_count = 0
    total_profit = 0

    with open(src_file, 'r') as f:
        for line in f:
            firm, _, rev, exp = line[:-1].split()
            profit = int(rev) - int(exp)
            if profit > 0:
                total_profit += profit
                positive_profit_count += 1
            res_dict[firm] = profit
    avr_profit = total_profit / positive_profit_count if positive_profit_count else 0
    res.append(res_dict)
    res.append({'average_profit': avr_profit})

    with open(dst_file, 'w') as f:
        json.dump(res, f)


def generate_sample_file(file_path, samples):
    """
    Generate file with lines formatted and data from samples
    :param file_path: str
    :param samples: list of tuple
    """
    with open(file_path, 'w') as f:
        for t in samples:
            f.write(' '.join(map(str, t)))
            f.write('\n')


if __name__ == '__main__':
    import os
    from pprint import pprint

    samples_file = 'task7_samples.txt'
    result_file = 'task7_profit.json'
    if not os.path.exists(samples_file):
        samples_example = [("firm_1", "OOO", 10000, 5000),
                           ("firm_2", "Gmbh", 20000, 7000),
                           ("firm_3", "LLC", 8000, 20000)]
        generate_sample_file(samples_file, samples_example)

    calculate_profit(samples_file, result_file)
    with open(result_file, 'r') as f:
        js = json.load(f)
        pprint(js, width=1)
