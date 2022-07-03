"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
    выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
    нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
    вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
    символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
    ранее сумме и после этого завершить программу.
"""

def calculate(*a):
    sum = 0
    sm = False
    for b in a:
        try:
            if b:
                sum += float(b)
        except ValueError:
            sm = True
    return sum, sm

calculate_sum = 0

while True:
    string = input('Введите числа через пробел: ').split(' ')
    sum, err_sm = calculate(*string)
    calculate_sum += sum
    print(f'Сумма чисел:,{calculate_sum}')

    if err_sm:
        break
