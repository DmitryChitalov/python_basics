"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""


def summary():
    try:
        with open('file_5.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел \n')
            file_obj.writelines(line)
            my_numb = line.split()

        with open('file_5.txt', 'r') as file:
            numbers_str = file.read()
            numbers_lst = numbers_str.split(' ')
            print(f"Содержимое файла:\n{numbers_str}")
            print(f"Сумма чисел:\n{sum([int(i) for i in numbers_lst])}")
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')
summary()
