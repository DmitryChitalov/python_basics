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

rus_text = ["Один ", "Два ", "Три ", "Четыре "]
convert_text = []
i = 0

with open("file.txt", encoding='utf=8') as f_obj:
    for line in f_obj:
        word = line.split(" ", 1)
        word[0] = rus_text[i]
        convert_text.extend(word)
        i += 1

with open("new_file.txt", "w", encoding='utf=8') as f_obj:
    f_obj.writelines(convert_text)
    print(convert_text)
