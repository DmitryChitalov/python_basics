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

def read_file(file_name):
    companies = {}
    total_profit = 0
    count_profitable = 0
    with open(file_name, 'r') as file:
        for line in file:
            data = line.strip().split()
            name, ownership, revenue, expenses = data[0], data[1], int(data[2]), int(data[3])
            profit = revenue - expenses
            companies[name] = profit
            if profit > 0:
                total_profit += profit
                count_profitable += 1
    if count_profitable > 0:
        average_profit = total_profit / count_profitable
    else:
        average_profit = 0
    return companies, average_profit

def save_to_json(file_name, data):
    """
    Сохранение данных в файл в формате json
    """
    with open(file_name, 'w') as file:
        json.dump(data, file)

if __name__ == '__main__':
    file_name = 'companies.txt'
    json_file_name = 'companies.json'
    companies, average_profit = read_file(file_name)
    result = [companies, {'average_profit': average_profit}]
    save_to_json(json_file_name, result)
    print(f'Result: {result}')
