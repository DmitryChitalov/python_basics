# Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
# Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.

def my_sum():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Введите строку чисел через пробел или знак ! для завершения: ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == '!':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Сумма чисел: {sum_res}')
    print(f'Окончательная сумма: {sum_res}')


my_sum()
