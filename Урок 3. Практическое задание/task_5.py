"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
    выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
    нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
    вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
    символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
    ранее сумме и после этого завершить программу.
"""



def my_func(args):
    if "+" in args:
        print('Boom Boom')
        res_ = ' '.join(args).replace('+', '').split()
        res = [int(item) for item in res_]
        is_continue_ = bool(0)
    else:
        args_ = args.split()
        res = [int(item) for item in args_]
        is_continue_ = bool(1)
    return sum(res), is_continue_


is_continue = bool(1)
numbers_ = 0

while is_continue:
    numbers = input("Введите числа через пробел: ")
    temp = my_func(numbers)
    numbers_ = numbers_ + temp[0]
    is_continue = temp[1]
    print(f"Сумма: {numbers_}")
