"""
6)	Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, 
практических и лабораторных занятий по этому предмету и их количество. 
Важно, чтобы для каждого предмета не обязательно были все типы занятий. 
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                     Физика:   30(л)   —   10(лаб)
                     Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
#!/usr/bin/env python3
import re

# re.sub(r'\([^)]*\)')

input_data = []
clear_data = {}
clear_value = []
subject_name = []
mediator_data = []
mediator_hours = []
plectrum_hours = []

with open("input_file6.txt") as input_source:
    
    for i in input_source:
        input_data.append(i)

    for j in input_data:
        # print(f"{(j.split()[0]).strip(':')}, {j.split()[1:]}")
        subject_name = j.split()[0].strip(':')
        mediator_hours = j.split()[1:]
        mediator_data = [k for k in mediator_hours if len(k) > 1]
        plectrum_hours = [re.sub(r'\([^)]*\)', '', plectrum) for plectrum in mediator_data]
        clear_value = [int(x) for x in plectrum_hours]
        clear_data[subject_name] = clear_value

    for dict_key, dict_value in clear_data.items():
        print(dict_key, "всего", sum(dict_value), "ч.")
        clear_data.update({dict_key: sum(dict_value)})
    
print(clear_data)
