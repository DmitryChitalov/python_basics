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
translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
rus = []
with open('test.txt', "r") as f_obj:
    with open('test_update.txt', 'w') as f_update:
        for i in f_obj:
            new = i.split(' ')
            if new[0] in translate:
                rus.append(i.replace(new[0], translate[new[0]]))
        f_update.writelines(rus)







