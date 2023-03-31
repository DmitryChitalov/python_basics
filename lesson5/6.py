"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб)
Физика: 30(л) - 10(лаб)
Физкультура: - 30(пр) -
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

subjects = {}
try:
    with open("6.txt", encoding='utf-8') as my_f:
        li = my_f.readlines()
    for line in li:
        data = line.replace('(', ' ').split()
        subjects[data[0][:-1]] = sum(int(i) for i in data if i.isdigit())
except ValueError:
    print("Ошибка")

print(subjects)