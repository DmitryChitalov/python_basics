"""
7)	Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
import json

profit = {}
average_profit = {}
loss = {}
finance = [profit, average_profit, loss]
try:
    with open("file1.txt", 'r', encoding='utf-8') as file:
        companies = file.readlines()
        for company in companies:
            delta = float(company.split()[2]) - float(company.split()[3])
            if delta < 0:
                loss[' '.join(company.split()[:2])] = delta
            else:
                profit[' '.join(company.split()[:2])] = delta
        average_profit["average_profit"] = sum(profit.values()) / len(profit)
        print(finance)
        with open("my_file.json", "w") as write_f:
            json.dump(finance, write_f)
except IOError:
    print("Ошибка ввода-вывода!")
