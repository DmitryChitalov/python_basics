"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
user_text = input("Введите текст: ").split()
print('')

file_name_and_path = '/Users/aleksandr_bolokhov/Desktop/GeekBrains/DevOps/Python/homeworks/python_basics/Урок 5. Практическое задание/task_1/user_text.txt'

try:
    with open(file_name_and_path, 'w', encoding='utf-8') as file:
        file.writelines('%s\n' % line for line in user_text)
except IOError:
    print('Что-то пошло не так!')
