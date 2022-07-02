"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

new_file = open(r'text.txt', 'w')
line = input('Введите текст: ')

while line:
    new_file.writelines(line)
    line = input('Введите текст: ')
    if not line:
        break

new_file.close()
new_file = open('text.txt', 'r')
text_file = new_file.readlines()
print(text_file)
new_file.close()