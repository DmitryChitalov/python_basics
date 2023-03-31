"""
6)	Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета необязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.

Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

example_dict = {}

with open('file.txt', 'r') as file:
    for i in file:
        date = i.rstrip('\n').split()
        date_1 = list(date[0])
        date_2 = date_1[:-1]
        count = 0

        for item in date[1:4]:

            list_cor = [int(item) if item.isdigit() else item for item in list(item)]
            a_list = [number for number in list_cor if type(number) is int]

            # for number in list_cor:
            #     if type(number) is int:
            #         a_list.append(number)
            #     else:
            #         list_cor.remove(number)

            my_str = ''.join(map(str, a_list))

            if len(my_str) >= 1:
                count += int(my_str)
            else:
                continue
        example_dict[''.join(date_2)] = count

print(example_dict)
