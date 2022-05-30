"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
with open('xyz.txt', 'w') as f:
    while True:
        user_input = input('Enter the value or ENTER to exit: ')
        if user_input:
            f.write(user_input + '\n')
        else:
            break


