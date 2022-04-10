"""
6)	Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

def my_replace(my_string):
    i = 0
    while i < 3:
        for my_substr in ['.', '\n', '(лаб)', '(л)', '(пр)']:
            if my_substr in my_string:
                my_string = my_string.replace(my_substr, '')
            i += 1

    if my_string.find("—") > -1 or my_string.find("-") > -1:
        my_string = '0'

    return int(my_string)


my_dict = {}

with open("my_file05_06.txt", "r", encoding='UTF8') as my_file_for_read:
    for my_row in my_file_for_read:
        if len(my_row) > 1:
            my_words = my_row.split(" ")
            my_dict[my_words[0]] = sum([my_replace(my_words[1]), my_replace(my_words[2]), my_replace(my_words[3])])

for my_dict_item_key, my_dict_item_value in my_dict.items():
    print(f"{my_dict_item_key} всего {my_dict_item_value} ч.")