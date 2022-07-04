from task_1.func import write_file

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

try:
    my_num = {
        "One": "1",
        "Two": "2",
        "Three": "3",
        "Four": "4",
        "Five": "5",
        "Six": "6",
        "Seven": "7",
        "Eight": "8",
        "Nine": "9",
        "Ten": "10"
    }

    with open("data.txt", encoding="utf-8") as f:
        for line in f:
            write_file("my_file.txt", line.replace(line.split(' ')[0], "" + my_num[line.split(' ')[0]]))

except BaseException as e:
    print(f"General error: {e}")


