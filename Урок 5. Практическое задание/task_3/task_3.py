"""
4)	Создать (не программно) текстовый файл со следующим содержимым:

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

try:
    with open("D:\TEST\\file1.txt") as f1_obj:
        for line in f1_obj:
            print(f"string= {line}")
            str1 = line
            str1 = str1.replace("One", "Один")
            str1 = str1.replace("Two", "Два")
            str1 = str1.replace("Three", "Три")
            str1 = str1.replace("Four", "Четыре")
            with open("D:\TEST\\file2.txt", "a") as f2_obj:  # а - режим на дозапись, а не перезапись файла как w
                print(str1, file=f2_obj)

except IOError:
    print("Произошла ошибка ввода-вывода!")
