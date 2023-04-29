"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
    выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
    нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
    вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
    символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
    ранее сумме и после этого завершить программу.
"""

nums = []
result = 0
flag_zero = False
flag = False

while True:
    number = input('\nВведите строку чисел: ').split()
    for inx, elem in enumerate(number):
        try:
            nums.append(int(elem))
        except ValueError:
            if inx == 0:
                flag_zero = True
                break
            flag = True
            break

    if not flag_zero and not flag:
        print(sum(nums))
    elif flag and not flag_zero:
        print(sum(nums))
        break
    else:
        break
