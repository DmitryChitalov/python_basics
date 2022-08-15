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
new_list = []
with open('one-two.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()
    for el in data:
        new_el = el.replace('One', 'Один')\
                   .replace('Two', 'Два')\
                   .replace('Three', 'Три')\
                   .replace('Four', 'Четыре')
        new_list.append(new_el)
with open('one-two-result.txt', 'w', encoding='utf-8') as f:
    f.writelines(new_list)
