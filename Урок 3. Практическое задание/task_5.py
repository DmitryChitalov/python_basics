"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
    выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
    нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
    вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
    символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
    ранее сумме и после этого завершить программу.
"""

def sums():
    result = 0
    while True:
        str_list = input("Enter integers and press Enter. For break, press Q: ").split()
        completion = False
        def converter(str_list):
            nonlocal completion
            int_list = []
            for val in str_list:
                if "Q" == val:
                    completion = True
                    return int_list
                int_list.append(int(val))
            return int_list

        for val in converter(str_list):
            result += val
        if completion:
            return result

print(sums())
