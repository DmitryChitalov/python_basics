"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
    выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
    нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
    вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
    символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
    ранее сумме и после этого завершить программу.
"""


def sum_user_input():
    sum_result = 0
    end_task = False
    while not end_task:
        user_digit = input("Введите числа через пробел. Для завершения ввода введите q: ").split()
        res = 0
        for i in range(len(user_digit)):
            try:
                if user_digit[i] == 'q':
                    end_task = True
                else:
                    res = res + int(user_digit[i])
            except ValueError:
                print('Введено недопустимое значение')
                break
        sum_result = sum_result + res
        print(f"Текущая сумма чисел равно: {sum_result}")
    return f"Конечная сумма всех чисел равна: {sum_result}"


print(sum_user_input())
