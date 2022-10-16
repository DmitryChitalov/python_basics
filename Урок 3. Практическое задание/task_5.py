"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
    выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
    нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
    вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
    символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
    ранее сумме и после этого завершить программу.
"""
total_sum = 0


def input_func():
    numb_list = input('Введите числа через пробел: ').split()
    print(f'Ваш список чисел: {numb_list}')
    sum_func(numb_list)


def sum_func(n_list):
    global total_sum
    try:
        for el in n_list:
            total_sum += int(el)
    except ValueError:
        print(f'Введён специальный символ, или некорректное значение. Итоговая сумма чисел - {total_sum}')
        exit()
    else:
        print(f'Сумма чисел на данный момент - {total_sum}')
    input_func()


input_func()
