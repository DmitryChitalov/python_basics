"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
my_file = open("lesson5-1.txt", "w", encoding="utf-8")
while True:
    string_list = input("Ввведите данные: ")
    if string_list == "":
        break
    my_file.writelines(string_list + "\n")
my_file.close()


with open("lesson5-1.txt", "r", encoding="utf-8") as my_file:
    print(my_file.read())