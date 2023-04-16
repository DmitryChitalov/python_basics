"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
with open('test.txt', 'w') as tfp:
    line = input('Введите текст (окончание - пустая строка):\n')
    while line:
        tfp.writelines(line + '\n')
        line = input('Введите текст (окончание - пустая строка):\n')
        if not line:
            break

with open('test.txt', 'r') as tfp:
    print(tfp.read())
