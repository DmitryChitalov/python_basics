"""
6)	Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

my_dict = dict()
with open('lessons.txt', 'r', encoding='utf-8') as my_file:
    for i in my_file:
        my_list = i.split()
        lessons_sum = 0
        for j in range(1, 4):
            if my_list[j] != '—':
                lessons_sum += int(my_list[j][:-5])
        my_dict[my_list[0]] = lessons_sum
print(my_dict)
