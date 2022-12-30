"""
6)	Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
with open('dz_6.txt', 'w', encoding="utf-8") as dz:
    i = ['Информатика: 100(л) 50(пр) 20(лаб)\n', 'Физика: 30(л) - 10(лаб)\n', 'Химия: - 30(пр) -\n']
    dz.writelines(i)
mydict = {}
with open("dz_6.txt", encoding='utf-8') as dz1:
    for y in dz1:
        name, stats = y.split(':')
        l_sum = sum(map(int, ''.join([i for i in stats if i == ' ' or ('0' <= i <= '9')]).split()))
        mydict[name] = l_sum
print(f"{mydict}")
