"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
my_f = open("dz_2.txt", "w", encoding='utf-8')
str_list = ['Заместитель командира по вооружению –\n', 'начальник отдела вооружения\n', 'войсковой части 00000\n']
my_f.writelines(str_list)
my_f.close()


my_f = open("dz_2.txt", "r", encoding='utf-8')
i = 1
for line in my_f:
    print(f'Параметры {i} строки')
    print(len(line), "символов")
    print(len(line.split()), "слов")
    i += 1
my_f.close()
