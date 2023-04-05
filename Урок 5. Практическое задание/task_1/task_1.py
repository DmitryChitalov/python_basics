"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
a = open("nata.txt", 'w')
text = []
while True:
    str = input("Введите данные или Enter для завершения: ")
    if str != '':
        text.append(str + "\n")
    else:
        break
a.writelines(text)

with open("nata.txt", "r") as a:
    content = a.readlines()
    print(content)

with open("nata.txt", "r") as a:
    for str in a:
        print(str)
