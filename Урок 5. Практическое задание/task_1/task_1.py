"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
file_open = open('my_file.txt', 'w')
while True:
    text_line = str(input("Text: \n"))
    if text_line == "print":
        file_open = open('my_file.txt', 'r')
        print("\nPrint file:\n-\n" + file_open.read() + "-f \nEnd file.")
        break
    elif not text_line:
        print("Exit.\n")
        break
    elif text_line:
        file_open.write(text_line + "\n")
file_open.close()
