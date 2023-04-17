"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

f_obj = open('my_file.txt', 'w')
while True:
    string = input('Информация для записи: ')
    f_obj.write(string + '\n')
    if string == '':
        break
f_obj.close()

with open('my_file.txt') as f_obj:
    content = f_obj.read()
    print(content)
    