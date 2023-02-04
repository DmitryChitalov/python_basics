"""
6)	Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
with open('les5_task6_text.txt', 'r', encoding='utf-8') as txt:
    dict_of_subjects = {line.strip().split(':')[0]: line.strip().split(':')[1].split() for line in txt}

def num_from_string(string):
    result = ''
    for i in string:
        if i.isdigit():
            result += i
        else:
            break
    if result != '':
        return int(result)
    else:
        return 0

for subject, content in dict_of_subjects.items():  
    current_subject = 0  
    for i in content:  
        current_subject += num_from_string(i)  
    dict_of_subjects[subject] = current_subject  

print(dict_of_subjects)
