"""
4)	Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
import os


cur_dir = os.path.join('Урок 5. Практическое задание', 'task_3')
file_path_read = os.path.join(cur_dir, 'one-two.txt')
file_path_write = os.path.join(cur_dir, 'one-two-result.txt')
new_list = []
with open(file_path_read, 'r', encoding='utf-8') as f:
    data = f.readlines()
    for el in data:
        new_el = el.replace('One', 'Один')\
                   .replace('Two', 'Два')\
                   .replace('Three', 'Три')\
                   .replace('Four', 'Четыре')
        new_list.append(new_el)
with open(file_path_write, 'w', encoding='utf-8') as f:
    f.writelines(new_list)
    print('Замена выполнена')
