"""
7)	Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""

import json

# Выводим задание для программы
print(f'\nНеобходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.\n'
      f'Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.\n'
      f'Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,\n'
      f'а также словарь со средней прибылью. Если фирма получила убытки,\n'
      f'также добавить ее в словарь (со значением убытков).\n')

# Объявляем переменные и открываем файл с исходными данными
input_file_name = 'firms.txt'
output_file_name = 'out_firms.json'
firm_profit = 0
total_profit = 0
firm_count = 0
firm_total = {}
total = []
input_file = open(input_file_name, encoding='utf-8')

# построчно вычисляем прибыль
for line in input_file:
    line_string = line.split()
    firm_profit = float(line_string[2]) - float(line_string[3])
    if firm_profit > 0:
        total_profit += firm_profit
        firm_count += 1
        print(f'Фирма "{line_string[0]}" имеет прибыль {"{:.2f}".format(firm_profit)}')
    elif firm_profit < 0:
        print(f'Фирма "{line_string[0]}" имеет убыток {"{:.2f}".format(firm_profit)}')
    elif firm_profit == 0:
        print(f'Фирма "{line_string[0]}" вышла в "ноль".')
    firm_total.update({line_string[0]: firm_profit})
input_file.close()

#расчет средней прибыли и добавление в список
total = (firm_total, {'Средняя_прибыль': total_profit / firm_count})

# Запись во внешний файл формата JSON
output_file = open(output_file_name, 'w+', encoding='utf-8')
json.dump(total, output_file, ensure_ascii=False)
output_file.seek(0)
print(output_file.read())
output_file.close()
