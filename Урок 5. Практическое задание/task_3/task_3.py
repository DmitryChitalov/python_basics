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
tr = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
tr_text = []
with open('task_3_en.txt', 'r', encoding="utf-8") as en:
    with open('task_3_ru.txt', 'w', encoding="utf-8") as ru:
        line = en.readlines()
        for i in line:
            i = i.split(' ', 1)
            tr_text.append(tr[i[0]] + ' ' + i[1])
        ru.writelines(tr_text)
