"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
test = open('test.txt', 'w')
line = input('Ввод \n')
while line:
    test.writelines(line)
    line = input('Ввод \n')
    if not line:
        break


test.close()
test = open('test.txt', 'r')
content = test.readlines()
print(content)
test.close()
