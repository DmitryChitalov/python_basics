"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
while True:
    out = input('Введите данные:')
    if out == '':
        break
    with open('data.txt', 'a') as f:
        f.write(f'{out}\n')
