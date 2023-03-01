"""
6)	Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
from functools import reduce
file_name_and_path = '/Users/aleksandr_bolokhov/Desktop/GeekBrains/DevOps/Python/homeworks/python_basics/Урок 5. Практическое задание/task_6/data.txt'

dic = {}
with open(file_name_and_path, 'r', encoding='utf-8') as file:
    my_data = file.read().splitlines()
    for line in my_data:
        key, value = line.split(': ')
        dic.update({key: value})
        
def sum_value_dic(dictionary):
    for key in dictionary:
        value_dic = ''
        for el in dictionary[key]:
            if el.isdigit():
                value_dic += str(el)
            else:
                value_dic += ' '
        sum_value_dictionary= reduce(lambda el_1, el_2: int(el_1) + int(el_2), value_dic.split())
        dictionary[key] = sum_value_dictionary
        
sum_value_dic(dic)    
print(dic)