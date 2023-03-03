"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

new_text = []
while True:
    el = input('Enter new string. Empty for stop: ')
    if el == '':
        break
    else:
        new_text.append(el)
with open('user_text.txt', 'a', encoding='utf-8') as file:
    file.writelines('%s\n' % line for line in new_text)


