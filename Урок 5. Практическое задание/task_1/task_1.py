"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
### пока пробую как работает print
with open("test_ivan.txt",
          "w") as f_obj:  # записываю новую строку в файл (при этом файл перезаписывается, если там что-то было, если нет файла, он создается
    print("Новая строка1 ", file=f_obj)
    print("Новая строка2 ", file=f_obj)
try:
    with open("test_ivan.txt") as f_obj:  # читаю файл  построчно, с проверкой наличия файла
        for line in f_obj:
            print(line)
except IOError:
    print("Произошла ошибка ввода-вывода!")

# Задача 1
a = "1"
with open("test_ivan.txt", "w") as f_obj:
    while a != "":
        a = input("Введите строку с данными: ")
        print(a, file=f_obj)

try:
    with open("test_ivan.txt") as f_obj:  # читаю файл  построчно, с проверкой наличия файла
        for line in f_obj:
            print(line)
except IOError:
    print("Произошла ошибка ввода-вывода!")
