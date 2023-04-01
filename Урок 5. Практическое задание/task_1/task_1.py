"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""


def user_data():
    """
    Создает список построчных данных, вводимых пользователем
    :return: Возращает список
    """
    new_list = []
    while True:
        try:
            new_string = input('Введите текст: ')
            if new_string == '':
                return [*new_list, '']
            new_list.append(new_string)
        except StopIteration:
            break


if __name__ == '__main__':
    try:
        print('Для выхода введите пустую строку.')
        strings = user_data()
        with open('my_file.txt', 'w', encoding='utf-8') as string_obj:
            string_obj.write('\n'.join(strings))
    except IOError:
        print('Ошибка при вводе данных!')
    except Exception as e:
        print(e)
