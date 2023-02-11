"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
def summary():
    try:
        with open('New_file.txt', 'w+') as file_obj:
            line = input('Введите целые числа через пробел: \n')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле. Попробуйте заново ввести числа.')
    except ValueError:
        print('Некорректно введены числа. Попробуйте заново ввести числа.')
summary()