"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

file_name = "test_file.txt"
out_f = open(file_name, "w")
print(f"Открыт на запись файл: {file_name}")
while True:
    file_string = input("Строка: >")
    if file_string == "":
        break
    else:
        out_f.write(file_string + "\n")

out_f.close()

