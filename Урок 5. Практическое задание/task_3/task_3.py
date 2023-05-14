"""
4)	Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

with open('text_file_3.txt', 'r', encoding='utf-8') as my_f, \
        open('text_file_3_new.txt', 'w', encoding='utf-8') as my_f_new:
    for line in my_f:
        my_string = line.split(' ')
        if my_string[0] == 'One':
            my_string[0] = 'Один'
        elif my_string[0] == 'Two':
            my_string[0] = 'Два'
        elif my_string[0] == 'Three':
            my_string[0] = 'Три'
        elif my_string[0] == 'Four':
            my_string[0] = 'Четыре'
        new_text = " ".join(my_string)
        my_f_new.write(new_text)
