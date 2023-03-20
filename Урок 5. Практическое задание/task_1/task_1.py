"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
my_file = open("out_file.txt", "w")
print("Введите строки:")
while bool(1):
    line = input()
    if line.strip():
        my_file.write(line)
        my_file.write("\n")
    else:
        my_file.close()
        break
