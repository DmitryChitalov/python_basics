"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

"""
Выполенине! Емельяненко А.А.
"""

my_fail = open('test1.txt', 'w')
line = input('Введите текст в файл \n')
while line:
    my_fail.writelines(line)
    line = input('Введите текст в файл \n')
    if not line:
        break

my_fail.close()
my_fail = open('test1.txt', 'r')
content = my_fail.readlines()
print(content)
my_fail.close()
