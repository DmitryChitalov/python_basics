"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
with open("out_text.txt", "w", encoding='utf-8') as f_out:
    lines = []
    print("Вводите данные, дважды нажмите 'Enter' для завершения")
    while True:
        line = input("")
        if line != '':
            lines.append(line + "\n")
        else:
            print("Данные записаны")
            break
    f_out.writelines(lines)