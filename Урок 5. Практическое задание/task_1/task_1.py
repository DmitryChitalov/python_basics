"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""


def create_strings():
    """
    create strings list
    :return: list strings
    :rtype: list[str]
    """
    lst = []
    while True:
        try:
            new_t = input('Input of string: ')
            if new_t == '':
                return [*lst, '']
            lst.append(new_t)
        except StopIteration:
            break


if __name__ == '__main__':
    try:
        print('# Exit: empty string and press Enter')
        strings = create_strings()
        with open('file.t', 'w') as f_obj:
            f_obj.write('\n'.join(strings))
    except IOError:
        print('Warning: error input output')
    except Exception as e:
        print(e)
