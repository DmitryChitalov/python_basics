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
dict_num = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open("note1.txt", "r") as note, open("note2.txt", "a", encoding="utf-8") as note2:
    for fstr in note:
        tstr = fstr.split()
        for wrd in tstr:
            if dict_num.get(wrd) is not None:
                note2.write(fstr.replace(wrd, dict_num.get(wrd)))
