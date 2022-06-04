"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
ls_1 = open('list_1.txt', 'w')
row_1 = input('Введите текст \n')
while row_1:
    ls_1.writelines(row_1)
    row_1 = input('Введите текст \n')
    if not row_1:
        break

ls_1.close()
row_1 = open('test.txt', 'r')
content = ls_1.readlines()
print(content)
ls_1.close()
