"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
f_file = open('my_text.txt','w')
line = input('Enter' + '\n')
while True:
    f_file.writelines(line + '\n' )
    line = input('Enter' + '\n')
    if not line:
        break


f_file.close()
with open('my_text.txt', 'r') as file:
    content = file.read()
    print(content)


