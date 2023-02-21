"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
my_file = open('test.txt', 'w', encoding='utf-8')
my_text = input('Ввод текста в файл \n')
while my_text:
    my_file.writelines(my_text)
    my_text = input('Ввод текста в файл \n')
    if not my_text:
        break