"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
    выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
    нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
    вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
    символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
    ранее сумме и после этого завершить программу.
"""


def sum_str(_sum, _inp_str):
    arr_str = str(_inp_str).split()
    arr_int = []
    for v in arr_str:
        if v == '!':
            break
        arr_int.append(int(v))
    return sum(arr_int) + _sum


sum_numbers = 0
while True:
    inp_str = input('Введите числа через пробел!')

    sum_numbers = sum_str(sum_numbers, inp_str)
    print(sum_numbers)
    if inp_str.count('!'):
        break
