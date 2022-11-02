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
out_f = open("text_file3.txt", "w", encoding='utf-8')
str_list = ['One — 1\n', 'Two — 2\n', 'Three — 3\n', 'Four — 4']
out_f.writelines(str_list)
out_f.close()

write_file = 'new_text_file3.txt'
with open("text_file3.txt", "r", encoding='utf-8') as f_obj, open(write_file, 'w', encoding='utf-8') as w_obj:
    for line in f_obj:
        clear_line = line.replace("(One)", "Один").replace("Two", "Два").replace("Three", "Три") \
            .replace("Four", "Четыре")
        w_obj.write(clear_line)
