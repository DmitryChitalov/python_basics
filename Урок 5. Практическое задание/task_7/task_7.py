"""
7)	Создать вручную и заполнить несколькими строками текстовый файл, 
в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
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
#!/usr/bin/env python3

input_data = []
winners_data = []
profit_calc = []
profitability_list = []
counter = 0
average_profit = []

with open("input_file7.txt") as input_source:
    for i in input_source:
        input_data.append(i)

    for j in input_data:
        print(j.strip())
        fiscal_data = j.split()
        if int(fiscal_data[2]) > int(fiscal_data[3]):
            winners_data.append(j.strip())

    for k in winners_data:
        profit_calc = k.split()
        
    for l in profit_calc:
        single_profit = [m for m in profit_calc if (int(profit_calc[2]) - int(profit_calc[3]) > 0)]
        profitability_list.append(single_profit)
    
    average_profit = sum(profitability_list) / len(winners_data)
    
    print(type(profitability_list), profitability_list)
    
    print(type(average_profit), average_profit)
