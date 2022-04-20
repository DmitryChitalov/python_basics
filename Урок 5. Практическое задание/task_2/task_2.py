"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

count_w = 0

with open("HW5_task2.txt", "r", encoding='utf-8') as f_obj:
    my_str = f_obj.readlines()
    count_l = len(my_str)

with open("HW5_task2.txt", "r", encoding='utf-8') as f_obj:
    my_str2 = f_obj.read()
    a = (my_str2.replace('\n', ' '))
    for el in a:
        if el == " ":
            count_w += 1

print(f"Количество строк - {count_l}, Количество слов - {count_w}")