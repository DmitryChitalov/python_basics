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

dict_numbers = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре"
}

with open("s_file.txt", "r", encoding="utf-8") as s_obj:
    tmp_text = []
    for line in s_obj.readlines():
        l_edit = line.split()
        l_edit[0] = dict_numbers[l_edit[0]]
        tmp_text.append(f"{l_edit[0].capitalize()} {l_edit[1]} {l_edit[2]}\n")
    with open("d_file.txt", "w", encoding="utf-8") as d_obj:
        d_obj.writelines(tmp_text)
