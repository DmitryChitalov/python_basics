"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
with open('task_1.txt', 'w', encoding="utf-8") as my_f:
    line = input('Введите текст \n ')
    while line:
        my_f.writelines(line)
        line = input('Введите текст \n ')
        if not line:
            break


