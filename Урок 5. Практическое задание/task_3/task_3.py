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
# Вариант 1
rus_numbers = ['Один — 1\n', 'Два — 2\n', 'Три — 3\n', 'Четыре — 4']

with open('task_3.txt', encoding='utf-8') as f_obj:
    read_lines = f_obj.readlines()

with open('rus_task_3.txt', 'w', encoding='utf-8') as f_obj:
    t = 0
    for i in range(0, len(read_lines)):
        read_lines[i] = rus_numbers[t]
        t += 1
    result = f_obj.writelines(read_lines)
print(f'Содержимое файла {f_obj.name}: \n {read_lines}')

# Вариант 2
rus_numbers = ['Один', 'Два', 'Три', 'Четыре']

with open('task_3.txt', encoding='utf-8') as f_obj:
    my_list = []
    for line in f_obj.readlines():
        my_list.extend(line.split(' '))

with open('var_2_rus_task_3.txt', 'w+', encoding='utf-8') as f_obj:
    t = 0
    for i in range(0, len(my_list), 3):
        my_list[i] = rus_numbers[t]
        t += 1
    my_list = ' '.join(my_list)
    result = f_obj.writelines(my_list)
print(f'Содержимое файла {f_obj.name}: \n {my_list}')
