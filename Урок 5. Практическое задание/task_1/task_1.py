"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
lst = list()
while True:
    in_str = input('Введите стоку: ')
    if in_str != '':
        lst.append(f'{in_str}\n')
    else:
        break
out_file = open('output.txt', 'w')
out_file.writelines(lst)
out_file.close()
