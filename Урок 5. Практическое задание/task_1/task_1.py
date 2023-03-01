"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

while True:
    user_input = input('Введите данные: ')
    if user_input == '':
        break
    else:
        with open("my_file.txt", 'a', encoding='utf-8') as my_file:
            my_file.write(user_input + '\n')
