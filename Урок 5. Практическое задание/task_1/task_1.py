"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""


def user_input(example):
    with open('file.txt', 'a') as file:
        file.write(f'{example} \n')


while True:
    check = input('Введите команду (add или exit): ').lower()

    if check == 'exit':
        break
    elif check == 'add':
        user_letter = input('Что добавим в file.txt? ')
        user_input(user_letter)
        print()

    else:
        print("Нет такой команды!")
