"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

from random import randint


def create_new_file():
    count = randint(0, 100)
    my_numbers = [str(randint(0, i)) for i in range(count)]
    with open('number.txt', 'w', encoding='utf-8') as string_obj:
        string_obj.write(' '.join(my_numbers))
    return my_numbers


if __name__ == '__main__':
    create_new_file()
    with open('number.txt', 'r', encoding='utf-8') as string_obj:
        print(f"Сумма чисел в файле: {sum([int(i) for i in string_obj.read().split()])}")
