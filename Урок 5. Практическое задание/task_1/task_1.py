"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
with open('task_1_text.txt','w', encoding='utf-8') as text_file:
    while True:
        enter_text = input('Enter some lines ')
        if not enter_text:
            break
        print(enter_text, file=text_file)
