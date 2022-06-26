"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
    выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
    нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
    вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
    символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
    ранее сумме и после этого завершить программу.
"""


def func_sum():
    total = 0
    exit_flag = False
    while exit_flag == False:
        number = input('Input numbers or Q for quit - ').split()

        result = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                exit_flag = True
                break
            else:
                result += int(number[el])
        total += result
        print(f'Current sum is {total}')
    print(f'Your final sum is {total}')


func_sum()
