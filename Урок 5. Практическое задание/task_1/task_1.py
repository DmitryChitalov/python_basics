"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

with open("out_file.txt", "w", encoding='utf=8') as f_obj:
    while True:
        input_text = input("Введите данные для записи в файл. Для окончании ввода введите пустую строку.\n>>> ")
        if input_text == "":
            print("Введена пустая строка, данные сохраняются, завершение работы программы.")
            break
        f_obj.writelines(input_text + '\n')
