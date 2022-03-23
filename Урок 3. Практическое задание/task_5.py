"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить
ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа
вводится специальный символ, выполнение программы завершается. Если специальный
символ введен после нескольких чисел, то вначале нужно добавить сумму этих
чисел к полученной ранее сумме и после этого завершить программу.
"""


def my_func():
    result = 0
    while True:
        numbers = input('Enter numbers through space. '
                        'Enter qqq for exit ').split()
        for i in numbers:
            try:
                if i == 'qqq':
                    print(f'The sum is {result}. Job is done')
                    return
                else:
                    result += int(i)
            except ValueError:
                print('Enter numbers or qqq for exit')
        print(f'The sum is {result}')


my_func()
