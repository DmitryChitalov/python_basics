# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

def summ():
    try:
        with open('dz5_5.txt', 'w+') as my_file:
            line = input('Введите цифры через пробел: ')
            my_file.writelines(line)
            my_numb = line.split()
            print(sum(map(int, my_numb)))
    except ValueError:
        print('Ошибка ввода! Можно вводить только цифры!')


summ()
