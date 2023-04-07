"""
6)	Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
import re

with open("text.txt", "r", encoding="utf-8") as f_obj:
    result = {}
    while True:
        content = f_obj.readline()
        if content == "":
            break
        content_without_brackets = re.sub(r'\([^()]*\)', '', content)
        content_split = content_without_brackets.split(" ")
        content_split = [line.rstrip() for line in content_split]
        content_numbers_split = [content_split[el] for el in range(1, len(content_split))]
        content_numbers = list(map(int, content_numbers_split))
        title = content_split[0].replace(":", "")
        result[title] = sum(content_numbers)
    print(result)

