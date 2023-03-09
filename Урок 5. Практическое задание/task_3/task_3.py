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
dictionary = dict()
dictionary.update({'One': 'Один'})
dictionary.update({'Two': 'Два'})
dictionary.update({'Three': 'Три'})
dictionary.update({'Four': 'Четыре'})

fw = open('numbers_rus.txt', 'w')
with open('numbers.txt', 'r') as f:
    for word in f:
        for (idx, number) in dictionary.items():
            word = word.replace(idx, number)
        fw.write(word)
fw.close()
