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


profit_firm = {}
average_revenue = {}
total_profit = 0
i = 0

with open('firm.txt', 'r', encoding='utf-8') as f_firm:
    for string in f_firm:
        name, firm, cash, cost = string.split()
        profit = int(cash) - int(cost)    #Высчитываем прибыль каждой фирмы по циклу
        if profit >= 0:
            profit_firm.update({name: profit})
            i += 1
        if i != 0:
            total_profit += profit
            average_revenue = {"average_profit": round(total_profit / i)}    #Высчитываем средний доход между фирмами
        else:
            print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    print(f"Отчет:\n[{profit_firm}, {average_revenue}]\n")

    with open('profit.json', 'w') as f_json:    #Записываем ответ в файл формата .json
        write_js = [profit_firm, average_revenue]
        json.dump(write_js, f_json)
        print(f"Создан файл с расширением json с содержанием: \n{write_js}")