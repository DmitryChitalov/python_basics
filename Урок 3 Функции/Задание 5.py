"""
5.Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter
должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и
снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее
сумме и после этого завершить программу.
"""

inp = input('Input integers with space or "/" for exit: ').split()


def suminp(inp):
    counter = 0

    def adding(input_v, counter):
        input_v = [int(i) for i in input_v]
        counter += sum(input_v)
        return counter

    if inp[-1] == '/':
        counter = adding(inp[:-1], counter)
        print(f'\nSum of integers before "/" is {counter}\n')
        return

    while inp != '' and inp[0] != '/':
        counter = adding(inp, counter)
        print(f'\nSum of integers is {counter}\n')

        inp = input('Input two integers with space ro "/" for exit: ').split()

        if inp[-1] == '/':
            counter = adding(inp[:-1], counter)
            print(f'\nSum of integers before "/" is {counter}\n')
            break

        if inp[0] == '/':
            print(f'\nSum of integers is {counter}\n')
            break


suminp(inp)
