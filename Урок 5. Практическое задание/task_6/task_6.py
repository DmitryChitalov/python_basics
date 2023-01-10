"""
6)	Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, 
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета 
не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий 
по нему. Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


subject_dictionary = {}
with open("file_task_6.txt", encoding='utf-8') as init_f:
    for line in init_f:
        temp = line.replace("(л)", "").replace("(пр)", "").replace("(лаб)", "").replace(".", "")
        subject, lecture, practice, lab = temp.split()

        temp_lecture = 0
        temp_practice = 0
        temp_lab = 0
     
        if lecture != "-":
            temp_lecture = int(lecture)
        if practice != "-":
            temp_practice = int(practice)
        if lab != "-":
            temp_lab = int(lab)
        
        subject_dictionary[subject] = temp_lecture + temp_practice + temp_lab
    print(f'{subject_dictionary}')