"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""


def solut():
    try:
        with open('text5.txt', 'w+') as text_char:
            row = input('Вводите цифры разделяя пробелами: \n')
            text_char.writelines(row)
            char = row.split()

            print(sum(map(int, char)))
    except ValueError:
        print('Ошибка! Вводите только числа!')


solut()
