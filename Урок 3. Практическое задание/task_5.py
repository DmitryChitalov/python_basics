"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
    выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
    нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
    вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
    символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
    ранее сумме и после этого завершить программу.
"""
first_list = input("Введите список чисел через пробел ")
result = 0
def sum_continuous_list(num_list, result):
    num_list = num_list.split(" ")
    if 'End' not in num_list:
        num_list = [int(el) for el in num_list]
        result = sum(num_list) + result
        print(result)
        new_input = input('Вы можете продолжить вводить числа или закончить работу, напечатав "End": ')
        if new_input == 'End':
            pass
        else:
            sum_continuous_list(new_input, result)
    else:
        num_list = [int(el) for el in num_list if el != 'End']
        result = sum(num_list) + result
        print(result)
        pass

print(sum_continuous_list(first_list, result))
