"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
    выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
    нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
    вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
    символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
    ранее сумме и после этого завершить программу.
"""


def my_sum ():
    val = 0
    num = False
    while num == False:
        # Цикл для остановки программы
        number = input('Введите цифру (X для выхода): ').split()
        res = 0
        for el in range(len(number)):
            if number[el] == 'x' or number[el] == 'X':
                num = True
                break
            else:
                res = res + int(number[el])
        val = val + res
        print(f'Значение сейчас: {val}')
    print(f'Ваше последнее значение: {val}')
my_sum()

