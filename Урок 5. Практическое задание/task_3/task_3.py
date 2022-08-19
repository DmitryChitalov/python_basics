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
translate_array = {"one": "один", "two": "два", "three": "три", "four": "четыре"}
try:
    f_read = open('lesson_5_3.txt', 'r', encoding="utf-8")
    f_write = open('lesson_5_3_output.txt', 'w', encoding="utf-8")

    for line in f_read:
        write_line = line.replace(line.split()[0], translate_array.get(line.split()[0].lower()).capitalize())
        try:
            f_write.write(write_line)
        except Exception as ex:
            print(f"ERROR: {ex}")
finally:
    f_read.close()
    f_write.close()
