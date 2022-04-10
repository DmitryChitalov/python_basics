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

def rewrit():
    t = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    nt = []
    try:
        with open('test.txt', 'r+', encoding="utf-8") as test:
            with open('new_test.txt', 'r+', encoding="utf-8") as new_test:
                l = test.readlines()
                for i in l:
                    i = i.split(' ', 1)
                    nt.append(t[i[0]] + ' ' + i[1])
                new_test.writelines(nt)
    except FileNotFoundError:
        return 'Файл не найден'
rewrit()