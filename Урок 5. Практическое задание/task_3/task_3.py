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

in_f = open('input.txt')
out_f = open('output.txt', 'w', encoding='utf-8')
in_lines = in_f.readlines()
out_lines = []
for line in in_lines:
    if line.count('One') == 1:
        out_lines.append(line.replace('One', 'Один'))
    if line.count('Two') == 1:
        out_lines.append(line.replace('Two', 'Два'))
    if line.count('Three') == 1:
        out_lines.append(line.replace('Three', 'Три'))
    if line.count('Four') == 1:
        out_lines.append(line.replace('Four', 'Четыре'))

out_f.writelines(out_lines)
in_f.close()
out_f.close()
