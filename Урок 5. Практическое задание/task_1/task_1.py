"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

with open('task1.txt', 'w', encoding='utf-8') as my_file:
    while True:
        lst = input("Введите текст: ")
        if lst == '':
            break
        else:
            my_file.writelines(lst + '\n')
with open('task1.txt', 'r', encoding='utf-8') as f_obj:
    content = f_obj.read()
    print(content)
