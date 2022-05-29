# Создать программно файл в текстовом формате, записать
# в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

my_file = open('my_file.txt', 'w')
line = input('Введите текст: ')
while line:
    my_file.writelines(line)
    line = input('Введите текст: ')
    if not line:
        break
    my_file.writelines(', ')

my_file.close()
my_file = open('my_file.txt', 'r')
content = my_file.readlines()
print(content)
my_file.close()
