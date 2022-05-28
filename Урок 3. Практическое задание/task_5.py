"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
    выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
    нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
    вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
    символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
    ранее сумме и после этого завершить программу.
"""

numbers_sum = 0

def update_sum(numbers_sum):
    new_numbers = input('Введите числа через пробел ==>').split()
    need_finish = False
    for item in new_numbers:
        if item.isdigit():
            numbers_sum += float(item)
        else:
            need_finish = True
            break
    print(f'Сумма: {numbers_sum}')
    if need_finish:
        print('Exited by user')
    else:
        update_sum(numbers_sum)

update_sum(numbers_sum)
 