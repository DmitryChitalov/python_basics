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

translation = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}


def new_word(trans_words):
    return translation[trans_words]


read_file = open("in_words.txt", "r")
new_file = open("out_words.txt", "w", encoding='utf-8')
line_num = 0
for read_line in read_file.readlines():
    if read_line != "\n":
        array_words = read_line.split(" - ")
        new_file.write(new_word(array_words[0]) + " - " + array_words[1])

read_file.close()
new_file.close()