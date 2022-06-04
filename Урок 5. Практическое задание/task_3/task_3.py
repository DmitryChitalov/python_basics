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
dictionary = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('Урок 5. Практическое задание/task_3/task_3.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()
    keys = dictionary.keys()
    for item in data:
        for key in keys:
            if key in item:
                line_out = item.replace(key, dictionary[key])
                with open('Урок 5. Практическое задание/task_3/result.txt', 'a', encoding='utf-8') as f_out:
                     f_out.write(line_out)
                
    