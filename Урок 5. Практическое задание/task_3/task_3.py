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

book = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
try:
    with open('t3.txt', 'r', encoding="utf-8") as t_obj:
        with open('t3.1.txt', 'w', encoding="utf-8") as t1_obj:
            for line in t_obj:
                st = line.split(' ', 1)
                st.insert(0, book[st.pop(0)])
                my = ' '.join(st)
                t1_obj.write(my)
except FileNotFoundError:
    print("Файл не найден!")
