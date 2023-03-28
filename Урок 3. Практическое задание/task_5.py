"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии user_input должна
    выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
    нажать user_input. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
    вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
    символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
    ранее сумме и после этого завершить программу.
"""
#!/usr/bin/env python3

sum_result = 0
special_sign = ''

def summing_func(string, list_index):
    user_input_list = string.split(" ")
    finished_list = []
    try:
        for i in user_input_list:
            list_index = i
            finished_list.append(int(i))
    except ValueError:
        return sum(finished_list), list_index
    return sum(finished_list), list_index

while special_sign != "q":
    user_input = input("Пожалуйста, введите строку чисел, разделенных пробелом, или 'q' для выхода: ")
    temporary_result, special_sign = summing_func(user_input, special_sign)
    sum_result = sum_result + temporary_result
    print(f"Текущий результат: {sum_result}")