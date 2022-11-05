"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
print("Вводите текс построчно, для завершения введите пустую строку.")
try:
    with open("user_text.txt", "w+", encoding="utf-8") as f_obj:
        while True:
            line = input(">")
            if line == "":
                break
            f_obj.write(f"{line}\n")

        print("Текущий файл:")
        f_obj.seek(0)
        print(f_obj.read())
except IOError:
    print("Произошла ошибка ввода вывода!")
