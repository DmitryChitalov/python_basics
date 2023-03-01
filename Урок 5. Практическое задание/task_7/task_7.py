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
file_name_and_path = '/Users/aleksandr_bolokhov/Desktop/GeekBrains/DevOps/Python/homeworks/python_basics/Урок 5. Практическое задание/task_7/data.txt'
json_name_and_path = '/Users/aleksandr_bolokhov/Desktop/GeekBrains/DevOps/Python/homeworks/python_basics/Урок 5. Практическое задание/task_7/data_file.json'
all_list = []
firms_and_profits = {}
average_profit = {}
loss_profit = {}
with open(file_name_and_path, 'r', encoding='utf-8') as file:
    my_data = file.read().splitlines()
    average_profit_list = []
    for line in my_data:
        firm, own, profit, loss = line.split() 
        if int(profit) - int(loss) >= 0:
            average_profit_list.append(int(profit) - int(loss))
            firms_and_profits.update({firm: int(profit) - int(loss)})
        else:
            loss_profit.update({firm: int(profit) - int(loss)})
    average_profit['average_profit'] = int(sum(average_profit_list) / len(average_profit_list))
    
all_list.append(firms_and_profits)
all_list.append(average_profit)
all_list.append(loss_profit)

with open(json_name_and_path, 'w') as file:
    json.dump(all_list, file)
    
