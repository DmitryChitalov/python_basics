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
list_rus = ['Один', 'Два', 'Три', 'Четыре']
correct_list = []
word_count = 0

with open("example.txt", "r") as file:

    for i in file:
        date = i.rstrip('\n').split()
        date[0] = list_rus[word_count]
        word_count += 1
        date = " ".join(date)
        correct_list.append(date)

with open("correct.txt", "a") as file:
    for i in correct_list:
        file.write(f'{i} \n')
