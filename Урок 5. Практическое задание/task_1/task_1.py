"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

def input_lines():
    print("Write lines, for exit enter empty string in the end")
    result = []
    while True:
        line = input(">> ")
        if line == "":
            break
        result.append(line + '\n')

    print("the end")
    return result

def write_lines(file_name, lines):
    file = open(file_name, "w", encoding="utf-8")
    file.writelines(lines)

def print_content(file_name):
    file = open(file_name, "r", encoding="utf-8")
    print(file.readlines())

lines = input_lines()
write_lines("output.txt", lines)
print_content("output.txt")


