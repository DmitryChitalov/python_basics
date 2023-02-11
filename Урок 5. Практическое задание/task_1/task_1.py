"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
FILENAME = "Text.txt"

if __name__ == "__main__":
    while True:
        user_input = input('Введите текст: ')
        if not user_input:
            break
        try:
            with open(FILENAME, 'a', encoding='utf-8') as fh:
                fh.write(f'{user_input}\n')
        except IOError as e:
            print(e)
            break
