"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
    выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
    нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
    вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
    символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
    ранее сумме и после этого завершить программу.
"""


def my_sum(my_list):
    summa = 0
    my_flag = True
    for number in my_list:
        try:
            next_number = int(number)
            summa += next_number
        except ValueError:
            my_flag = False
            return summa, my_flag
    return summa, my_flag


my_flags = True
sum_total = 0
while my_flags is True:
    my_str = input("Введите сроку чисел через пробел, они будут просуммированы. Любой символ кроме цифры завершит "
                   "суммирование.: ").split()
    my_str.insert(0, sum_total)
    sum_total, my_flags = my_sum(my_str)
    print(sum_total)
