"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
with open('user_data.txt', 'a', encoding='utf-8') as u_data:
    while True:
        user = input('Введите данные: ') + '\n'
        if user.strip() == '':
            break
        else:
            u_data.write(user)
