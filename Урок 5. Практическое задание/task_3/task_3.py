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

eng_ru = {'One': 'Один',
          'Two': 'Два',
          'Three': 'Три',
          'Four': 'Четыре'
          }


with open('file.txt', 'r', encoding='utf-8') as file:
    for key, value in eng_ru.items():
        files = file.readline().replace(key, value)
        with open('file_ru.txt', 'a', encoding='utf-8') as file_ru:
            file_ru.writelines(files)
