"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
my_list = open('text.txt', 'w', encoding='utf-8')
line = input('Введите текст \n')
while line:
    my_list.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break

my_list.close()
my_list = open('text.txt', 'r', encoding='utf-8')
content = my_list.readlines()
print(content)
my_list.close()