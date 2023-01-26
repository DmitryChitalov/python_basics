"""Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""

with open('file_1.txt', 'w', encoding='utf8') as f:
    st = True
    while st:
        st = input('Enter some data or press "Enter" for exit: ')
        f.write(st + '\n')
