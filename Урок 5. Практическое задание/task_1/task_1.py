"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
new_text = []
while True:
    el = input('Введите новую строку. Пробел для заврешения ввода: ')
    if el == '':
        break
    else:
        new_text.append(el)
with open('text.txt', 'a', encoding='utf-8') as file:
    file.writelines('%s\n' % line for line in new_text)