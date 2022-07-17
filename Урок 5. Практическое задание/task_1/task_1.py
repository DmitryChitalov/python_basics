"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

my_file = open('my_file.txt','w', encoding='utf-8')
line  = input ('Введите данные:' + '\n')
while True:
    my_file.writelines(line  + '\n')
    line = input('Введите данные:' + '\n')
    if not line:
        break

my_file.close()
with open('my_file.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print (content)
