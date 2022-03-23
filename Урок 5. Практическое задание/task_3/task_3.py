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
rus = ['Один', 'Два', 'Три', 'Четыре']
with open('task_3_text.txt', 'r+', encoding='utf-8') as file:
    word_list = list()
    for line in file.readlines():
        word_list.extend(line.split(' '))
r = 0
for e in range(0, len(word_list), 3):
    word_list[e] = rus[r]
    r += 1
out_file = open('task_3_text_new.txt', 'w', encoding='utf-8')
out_file.writelines(word_list)
out_file.close()
