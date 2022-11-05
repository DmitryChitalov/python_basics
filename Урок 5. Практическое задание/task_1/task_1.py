"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""


user_input = "."  # Объявляем переменную
out_f = open("data.txt", "w+", encoding="utf-8")
while True:
    user_input = input("Введите строку, которую необходимо записать в файл. "
                       "Для выхода из программы просто нажмите enter: ")
    if user_input == "":
        break
    out_f.write(user_input + "\n")

out_f.close()

with open("data.txt") as my_file:
    print(my_file.read())
