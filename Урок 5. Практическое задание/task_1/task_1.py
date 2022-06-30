"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
text = []

while True:
    with open('task1.txt', 'a+') as f:
        text = input("Input string: ")

        if not text:
            break
        f.write(f"{text}\n")
