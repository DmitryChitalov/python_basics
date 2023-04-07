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

with open("text.txt", "r") as f_obj:
    counter = 0
    while True:
        content = f_obj.readline()
        print(content)
        if content == "":
            break
        my_list = ["Один", "Два", "Три", "Четыре"]
        content_split = content.split(" ")
        content_split[0] = my_list[counter]
        counter += 1
        with open("new.txt", "a", encoding="utf-8") as w_obj:
            print(" ".join(content_split), file=w_obj)

