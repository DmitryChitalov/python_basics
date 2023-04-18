"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
print("Создание файла file_1.txt")
my_f1 = open("file_1.txt", "w")
while True:
    str_1 = input("Введите текст (для завершения нажмите Ввод):  ")
    if not str_1:
        break
    #my_f1.write(str_1)
    print(str_1, file=my_f1)
my_f1.close()
my_f1 = open("file_1.txt", "r")
b = my_f1.read()
print(b)
my_f1.close()
