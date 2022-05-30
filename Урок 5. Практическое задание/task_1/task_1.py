"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

INPUT_TEXT = 'Enter the data (empty string - exit): '

with open('file_1.txt', 'w', encoding='utf-8') as file:
    some_user_data = input(INPUT_TEXT)
    while some_user_data:
        file.write(f'{some_user_data}\n')
        # print(some_user_data, file=file)
        some_user_data = input(INPUT_TEXT)
