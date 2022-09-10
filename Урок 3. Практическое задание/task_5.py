"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
    выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
    нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
    вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
    символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
    ранее сумме и после этого завершить программу.
"""

user_string = input(f'Введите числа через пробел: ')

user_string = input(f'Введите числа через пробел: ')


def my_func(user_string):
    global result
    global bad_result
    bad_result = 0
    try:
        list1 = list(user_string.split())
        list2 = list(map(int, list1))
        result = sum(list2)
    except ValueError:
        list3 = list(user_string.split())
        for i in list3:
            if i.isdigit():
                a = int(i)
                bad_result += a
        return bad_result
    return result


final_summ = 0
while my_func(user_string) is not bad_result:
    final_summ += my_func(user_string)
    print(f'Сумма чисел: {final_summ}')
    user_string = input(f'Введите числа через пробел: ')
final_summ += my_func(user_string)
print(f'Сумма чисел: {final_summ}')
print('закончили')
