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

from json import dumps

my_dict_firm_profit = {}
my_dict_average_profit = {}

with open("my_file05_07.txt", "r", encoding='UTF8') as my_file_for_read:
    my_positive_profit_firms_count = 0
    my_total_profit = 0

    for my_row in my_file_for_read:
        if len(my_row) > 1:
            my_words = my_row.split(" ")
            my_profit = int(my_words[2]) - int(my_words[3])

        if my_profit >= 0:
            my_positive_profit_firms_count += 1
            my_total_profit += my_profit

        my_dict_firm_profit[my_words[0]] = my_profit

    my_dict_average_profit['average_profit'] = round(my_total_profit / my_positive_profit_firms_count, 2)

my_list = [my_dict_firm_profit, my_dict_average_profit]
json_string = dumps(my_list)

with open("my_file05_07.json", "w", encoding='UTF8') as my_file_for_write:
    my_file_for_write.write(json_string)
