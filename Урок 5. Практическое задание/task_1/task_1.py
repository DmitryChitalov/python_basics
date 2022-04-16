"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
my_str = '222'
my_list = []
while my_str != '':
    my_str = input("Enter str  для окачания введите enter ")
    if my_str != '':
        my_list.append(my_str)
with open("test.txt", 'w', encoding='utf-8') as my_file:
    my_file.writelines('\n' + line for line in my_list)
try:
    with open('test.txt', 'r', encoding='utf-8') as my_file:
        content = my_file.read()
    print(content)
except FileNotFoundError:
    print(f'Error')
