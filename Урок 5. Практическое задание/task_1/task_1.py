"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
with open('task_1.txt', 'w', encoding='utf-8') as my_file:
    while True:
        str_line = input('Введите строку: ')
        if not str_line:
            break
        print(str_line, file=my_file)
