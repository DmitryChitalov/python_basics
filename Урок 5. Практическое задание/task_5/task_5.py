"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""


def summary():
    try:
        with open('list_1.txt', 'w+') as list_obj:
            line = input('Enter numbers separated by spaces \n')
            list_obj.writelines(line)
            numb_1 = line.split()

            print(sum(map(int, numb_1)))
    except IOError:
        print('Error')
    except ValueError:
        print('Enter numbers separated by spaces ')


summary()
