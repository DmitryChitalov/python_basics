"""
6)	Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

def extract_num(str):
    num = str[:str.find("(")]
    if num.isdigit():
        return int(num)
    
    return 0

def parse_file(file_name):
    result = {}
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            print(line)
            values = line.split()
            if (len(values) < 4):
                print(f'{line}: wrong format')
                continue
            print(values)
            name = values[0]
            lectures = extract_num(values[1])
            practices = extract_num(values[2])
            labs = extract_num(values[3])
            result[name] = lectures + practices + labs
    return result

dict = parse_file("input.txt")
print(dict)