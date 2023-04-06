"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
out_f = open("out_file.txt", "w")
text = []
i = -1
while i == -1:
    string = input("Введите текст или нажмите Enter для окончания ввода: ")
    if string != '':
        text.append(string +"\n")
    else:
        break
out_f.writelines(text)
out_f.close()
