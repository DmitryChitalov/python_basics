"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
my_f = open("test.txt", "w", encoding='utf-8')
my_text = input("Введите текст в файл: ")

while my_text != '':
    my_f.writelines(my_text + ' ')
    my_text = input()


my_f.close()

my_f = open("test.txt", "r", encoding='utf-8')
print(my_f.readline())
my_f.close()