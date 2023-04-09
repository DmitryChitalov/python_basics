"""6)	Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета
не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий
по нему. Вывести словарь на экран. Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб). Физика:   30(л)   —
  10(лаб) Физкультура:   —   30(пр)   — Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}"""

import os

path = os.path.dirname(__file__)

input_list = []


def replace_symbols(r_string):
    text = r_string
    symbols = ['(лаб)', '(пр)', '(л)', "\n"]
    for symbol in symbols:
        if symbol in text:
            text = text.replace(symbol, '')
    if "-" in text:
        text = text.replace("-", '0')
    return text


my_dict = {}
with open((os.path.join(path, 'lessons.txt')), "r") as file_r:
    for line in file_r:
        result = 0
        string = line
        string = replace_symbols(string)
        input_list = string.split()
        result = result + int(input_list[1]) + int(input_list[2]) + int(input_list[3])
        my_dict.update({input_list[0]: result})

print(my_dict)

