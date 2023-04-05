"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
    выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
    нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
    вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
    символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
    ранее сумме и после этого завершить программу.
"""
def summ_list():
    res = 0
    while True:
        numbers_list = input('Введите числа через пробел или * для выхода: ').split()
        for i in numbers_list:
            try:
                if i == '*':
                    print(f'Сумма аргументов составляет: {res}. Выход из программы.')
                    quit()
                else:
                    res += int(i)
            except ValueError:
                print('Введите число или * для выхода')
        print(f'Сумма на текущий момент: {res}')

summ_list()