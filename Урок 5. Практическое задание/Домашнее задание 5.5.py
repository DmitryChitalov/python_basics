# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

def sum_():
    try:
        with open('task_5.txt', 'w') as out_f:
            line = input('Введите цифры через пробел \n')
            out_f.writelines(line)
            numb = line.split()
            print(sum(map(int, numb)))
    except ValueError:
        print('Ошибка')


sum_()