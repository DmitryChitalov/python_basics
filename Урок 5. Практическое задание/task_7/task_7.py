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

with open('les5_task7_text.txt', 'r', encoding='utf-8') as txt:
    dict_of_firms = {line.strip().split()[0]: int(line.strip().split()[2]) - int(line.strip().split()[3]) for
                     line in txt}
# подсчет средней прибыли (только для компаний с прибылью)
sum_profit = 0  
profitable_firms = 0  
for value in dict_of_firms.values():
    if value >= 0:  
        sum_profit += value  
        profitable_firms += 1  
average_profit = sum_profit / profitable_firms  # расчет средней прибыли
# создание списка из 2х словарей
list_of_firms = [dict_of_firms, {"average_profit": average_profit}]
# заись json-объекта в файл
with open('les5_task7_text2.json', 'w') as txt:
    json.dump(list_of_firms, txt)
