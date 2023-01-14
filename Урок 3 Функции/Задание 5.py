"""
5.Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter
должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и
снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее
сумме и после этого завершить программу.
"""

str = input('Input integers with space or "/" for exit: ').split()
counter = 0


def sumstr(string):
    global counter
    while string != '':
        # специальный символ введен после нескольких чисел
        if len(string) >= 3 and string[-1] == '/':
            string.pop()
            string = [int(i) for i in string]
            counter += sum(string)
            print(f'Sum of integers after "/" is {counter}')
            break
        # специальный символ, выполнение программы завершается
        if string and string[0] == '/':
            break
        else:
            # для проверки неверного введения числа (напрмер: 1 2/) --------------------------------------------------
            try:
                string = [int(i) for i in string]
            except ValueError:
                a = False
                while a is False:
                    string = input(
                        f'Input ONLY integers, you entered wrong data {string}: ').split()
                    # специальный символ введен после нескольких чисел
                    if len(string) >= 3 and string[-1] == '/':
                        string.pop()
                        string = [int(i) for i in string]
                        print(f'Sum of integers after "/" is {counter}')
                        break
                    try:
                        string = [int(i) for i in string]
                        a = True
                    except ValueError:
                        pass

            # --------------------------------------------------------------------------------------------------------
            counter += sum(string)
            print(f'\nSum of integers is {counter}\n')

        string = input(
            'Input two integers with space ro "/" for exit: ').split()


sumstr(str)
