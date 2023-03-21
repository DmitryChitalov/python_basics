"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

txt_file = open('new_file.txt', 'w', encoding='utf-8')
while True:
    text = input('Введите текст для записи в файл: ')
    txt_file.write(f'{text}\n')
    if not text:
        break
txt_file.close()
