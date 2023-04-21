__author__ = 'AndreiM'
__version__ = "1.0 18.04.2023"
print("\n task_5 \n -------- \n")

"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

filename = 'text_5.txt'

def summ():
    try:
        with open(filename, 'w+', encoding='utf-8') as f:
            line = input('Введите числа через пробел:   ')
            f.writelines(line)
            numb = line.split()
            print(sum(map(float, numb)))
    except IOError:
        print('Error. Невозможно создать файл')
    except ValueError:
        print('Вы ввели недопустимый формат. Необходимо вводить только числа!')
summ()