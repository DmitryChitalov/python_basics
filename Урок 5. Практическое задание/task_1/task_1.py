"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
with open('task_1.txt', 'w', encoding='utf-8') as f_obj:
    while f_obj:
        result = input('Введите данные: ')
        f_obj.write(result + '\n')
        if not result:
            break
