"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from random import randint

AMOUNT_NUMBERS = 12


def create_num_file(max_num):
    if isinstance(max_num, int):
        lst = [str(randint(0, i)) for i in range(max_num)]
        try:
            with open('text', 'w') as f_obj:
                f_obj.write(' '.join(lst))
            return True
        except IOError:
            return False
    else:
        return False


if __name__ == '__main__':
    if create_num_file(AMOUNT_NUMBERS):
        try:
            with open('text', 'r') as f_obj:
                print(f"Сумма чисел в файле: {sum([int(i) for i in f_obj.read().split()])}")
        except IOError:
            print('Warning: error input output')
