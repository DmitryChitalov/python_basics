"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
file = open("test.txt", 'w', encoding='utf-8')
lines = []
while True:
    line = input("Введите данные построчно или нажмите Enter для завершения: ")
    if line != '':
        lines.append(line)
    else:
        break
for word in lines:
    file.writelines(word + '\n')
