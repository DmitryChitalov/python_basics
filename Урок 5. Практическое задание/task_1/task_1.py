"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
try:
    with open("my_file.txt", 'w', encoding='utf-8') as file:
        text = []
        while True:
            line = input()
            if len(line) == 0:
                break
            else:
                text.append(f'{line}\n')
        file.writelines(text)
except IOError:
    print("Ошибка ввода-вывода!")
