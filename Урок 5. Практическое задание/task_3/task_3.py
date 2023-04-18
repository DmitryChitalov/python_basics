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
with open("input_file.txt", "r", encoding='utf-8') as f1_obj:
    with open("ouput_file.txt", "w", encoding='utf-8') as f2_obj:
        eng_list = ['One', 'Two', 'Three', 'Four']
        rus_list = ['Один', 'Два', 'Три', 'Четыре']
        for line in f1_obj:
            for i in range(0, 4):
                line = line.replace(eng_list[i], rus_list[i])
            f2_obj.write(line)
