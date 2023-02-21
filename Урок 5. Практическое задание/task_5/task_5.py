"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

def summ_programm():
    try:
        with open('file_summ.txt', 'w+') as file_obj:
            line = input('Введите набор чисел, разделенных пробелами \n')
            file_obj.writelines(line)
            my_summ = line.split()

            print(sum(map(int, my_summ)))
    except ValueError:
        print('Ошибка ввода')

summ_programm()