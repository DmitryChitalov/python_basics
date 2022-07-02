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

with open('file3.txt', 'r+', encoding='utf-8') as file:
    lst = list()
    for line in file.readlines():
        lst.extend(line.split(' '))
print(lst)

rus_lst = ["Один", "Два", "Три", "Четыре"]

j = 0
for i in range(0, len(lst), 3):
    lst[i] = rus_lst[j]
    j += 1

print(lst)
out_f = open('file3_new.txt', 'w', encoding='utf-8')
out_f.writelines(lst)
out_f.close()

