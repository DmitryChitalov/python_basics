"""
6)	Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету
и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика:   100(л)   50(пр)   20(лаб).
Физика:   30(л)   —   10(лаб)
Физкультура:   —   30(пр)   —

Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

try:
    lec_sum = 0
    practice_sum = 0
    lab_sum = 0

    res_dict = {}

    with open("data.txt", encoding='utf-8') as f:
        for line in f:
            dict_line = line.replace("(л)", "").\
                replace("(пр)", "").replace("(лаб)", "")\
                .replace(".", "").replace(":", "")

            if dict_line.split()[1] != "-":
                lec_sum = int(dict_line.split()[1])
            if dict_line.split()[2] != "-":
                practice_sum = int(dict_line.split()[2])
            if dict_line.split()[3] != "-":
                lab_int = int(dict_line.split()[3])

            res_dict[dict_line.split()[0]] = lec_sum + practice_sum + lab_sum

        print(f"{res_dict}")

except BaseException as e:
    print(f"General error: {e}")

except IOError as e:
    print(f"IOError: {e}")
