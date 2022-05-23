"""
6)	Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
 практических и лабораторных занятий по этому предмету и их количество.
 Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь,
содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


def get_subject(some_str):
    word = ""
    number_str = ""
    subject = {}
    i = 0
    while some_str[i] != ":":
        word = word + some_str[i]
        i += 1
    subject[word] = 0
    while i != len(some_str):
        if some_str[i].isnumeric():
            number_str += some_str[i]
        if number_str != "" and some_str[i] == " ":
            subject[word] += float(number_str)
            number_str = ""
        i += 1
    if number_str != "":
        subject[word] += float(number_str)
    return subject


def merge_dicts(dict1, dict2):
    res = dict1.copy()
    res.update(dict2)
    return res


input_file = open('inputtextfile.txt', 'r')

result = {}
for line in input_file:
    result = merge_dicts(result, get_subject(line))
print(result)
input_file.close()
