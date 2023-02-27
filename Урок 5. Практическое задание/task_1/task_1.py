"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

input_text = open('input_text', 'w')
while True:
    text_string = input('Введите текст: ')
    if text_string == '':
        break
    input_text.write(text_string+'\n')
input_text.close()
