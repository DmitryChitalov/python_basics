"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
import os


cur_dir = os.path.join('Урок 5. Практическое задание', 'task_1')
file_path = os.path.join(cur_dir, 'result.txt')
while True:
    user_val = input('Введите строку: ')
    if user_val == '':
        break
    with open(file_path, 'a', encoding='utf-8') as f:
        f.writelines(user_val + '\n')
with open(file_path, 'r', encoding='utf-8') as f:
    print(f.read())
    