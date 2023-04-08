"""
7)	Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные
о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней
прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
import json
res = {}
earning = 0
n = 0
company = {}
with open("lesson5-7.txt", "r", encoding="utf-8") as my_file:
    for line in my_file:
        name, num, profit, loss = line.split()
        res[name] = int(profit) - int(loss)
        if res.setdefault(name) >= 0:
            earning = earning + res.setdefault(name)
            n = n + 1
    if n != 0:
        sum_profit = earning / n
        print(f"Средний заработок составляет {sum_profit}")
    else:
        print(f"Прибыли нет")
    company = {}

with open("lesson5-6.json", "w") as my_json:
    json.dump(sum_profit, my_json)

    json_str = json.dumps(res)
    print(f"Companies income: {json_str}")