"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
f_obj = ("text_1.txt", encoding='utf-8')
lines =[]
while True:
    line = input("Введите новые данные или введите Enter для завершения: ")
    if line != '':
        lines.append(line + "\n")
    else:
        break
f_obj .writelines(lines)

with open("text_1.txt", "r", encoding='utf-8') as f_obj:
    content = f_obj.readlines()
    print(content)

with open("text_1.txt", "r", encoding='utf-8') as f_obj:
    for line in f_obj:
        print(line)

