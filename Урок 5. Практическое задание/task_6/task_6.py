"""
6)	Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


def number_in_str(var_str):
    result = ""
    for i in var_str:
        if i.isdigit():
            result = result + i
    try:
        result = int(result)
    except ValueError:
        result = 0
    return result


article = {}
my_file = open("text7.txt", "r", encoding="utf-8")
while True:
    line = my_file.readline()
    if not line:
        break
    lst_line = line.split()
    result = 0
    for i in lst_line:
        result += number_in_str(i)
    article[lst_line[0].replace(":", "")] = result
my_file.close()
print(article)
