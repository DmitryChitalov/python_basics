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
exist_file = open("txt.txt", "r", encoding='utf-8')
text = exist_file.readline()
text = text[:-1]
with open("russian.txt", "w", encoding='utf-8') as r:
    print(text.replace('One', 'Один'), file=r)

text = exist_file.readline()
text = text[:-1]
with open("russian.txt", "a", encoding='utf-8') as r:
    print(text.replace('Two', 'Два'), file=r)

text = exist_file.readline()
text = text[:-1]
with open("russian.txt", "a", encoding='utf-8') as r:
    print(text.replace('Three', 'Три'), file=r)

text = exist_file.readline()
with open("russian.txt", "a", encoding='utf-8') as r:
    print(text.replace('Four', 'Четыре'), file=r)