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

MY_DICT = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
}

file_in = './task_3/my_text.txt'

with open(file_in, 'r', encoding="UTF-8") as fl:
    # print(fl.readlines())
    all_words = fl.readlines()

with open('NewFile.txt', 'w+', encoding="UTF-8") as nf:
    for words in all_words:
        word = words.split()
        print(f"{MY_DICT.get(word[0])} {word[1]} {word[2]}", file=nf)
