"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""


def summary():
    """Формула ввода и подсчета чисел"""
    try:
        with open('file_task_5.txt', 'w+', encoding='utf-8') as file:
            line = input('Введите цифры через пробел: ')
            file.writelines(line)
            my_numb = line.split()
            print(sum(map(int, my_numb)))
    except ValueError:
        print('Ошибка ввода-вывода')


summary()
