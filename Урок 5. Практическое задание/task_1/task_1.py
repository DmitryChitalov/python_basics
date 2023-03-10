"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
with open("data.txt", "w", encoding='utf-8') as f_obj:
     lines = []
     while True:
        line = input("Введите данные или нажмите Enter для выхода: ")
        if line != '':
            lines.append(line + "\n")
        else:
            break
        f_obj.writelines(lines)

