"""
6)	Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

academic_subject = {}

def subject_time(string):
    words = string.split()
    while True:
        try:
            words.remove("-")
        except Exception:
            break

    hours = []
    for word in words:
        num = ""
        for char in word:
            if char.isdigit():
                num += char
        try:
            hours.append(int(num))
        except Exception:
            continue
    return sum(hours)


with open("info.txt", "r") as f:
    info = f.readlines()
    for string in info:
        words = string.split()
        academic_subject[words[0]] = subject_time(string)

print(academic_subject)
