"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
line = input('Введите текст: ')

with open('test.txt', 'w') as my_file:
    print(line, file=my_file)

my_f = open('test.txt', 'r', encoding='utf-8')
content = my_f.read()
print(content)
my_f.close()
