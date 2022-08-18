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

with open("file_3.txt", "r", encoding="utf-8") as f_obj:
    content = f_obj.read()

    with open("file_3_3.txt", "a", encoding="utf-8") as f_obj_new:
        print(content
              .replace("One", "Один")
              .replace("Two", "Два")
              .replace("Three", "Три")
              .replace("Four", "Четыре"),
              file=f_obj_new)
