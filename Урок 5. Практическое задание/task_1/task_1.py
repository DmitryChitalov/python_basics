"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
while True:
    user_val = input('Введите строку: ')
    if user_val == '':
        break
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.writelines(user_val + '\n')
with open('result.txt', 'r', encoding='utf-8') as f:
    print(f.read())
    