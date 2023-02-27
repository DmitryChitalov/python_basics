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
    numb = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    at = []
    try:
        with open('03.txt', 'r+', encoding="utf-8") as text:
            with open('03tr.txt', 'r+', encoding="utf-8") as tr_text:
                a = text.readlines()
                for b in a:
                    b = b.split(' ', 1)
                    at.append(numb[b[0]] + ' ' + b[1])
                tr_text.writelines(at)
    except FileNotFoundError:
        return 'Файл не найден'
rewrit()
