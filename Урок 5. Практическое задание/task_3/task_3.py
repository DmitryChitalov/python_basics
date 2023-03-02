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
rep_inp = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("less5_t3_numb.txt", encoding='utf-8') as f_obj:
    for line in f_obj:
        for key in rep_inp.keys():
            line = line.replace(key, rep_inp[key])
        print(line)
        with open("less5_t3_rusn.txt", 'a', encoding='utf-8') as t_rus:
            t_rus.write(f"\n {line}")