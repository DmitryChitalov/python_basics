"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
my_list_str = []
out_f = open("task1.txt", "w", encoding='utf-8')
while True:
    my_str = input("Введите Вашу строку: ")
    if my_str != "":
        my_list_str.append(my_str + "\n")
    else:
        break
out_f.writelines(my_list_str)
out_f.close()
