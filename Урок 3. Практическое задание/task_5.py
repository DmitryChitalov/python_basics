"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
    выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
    нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
    вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
    символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
    ранее сумме и после этого завершить программу.
"""

from typing import Tuple
import string_extension

def sum_num_list(num_list) -> float:
    sum = 0
    for val in num_list:
        sum += val
    return sum

def sum_input_numbers(value, stop_word) -> Tuple[float, bool]:
    float_list, is_all_float, not_float_value = string_extension.to_float_list(value, " ")
    if is_all_float:
        return sum_num_list(float_list), True
    elif not_float_value == stop_word:
        return sum_num_list(float_list), False
    else:
        print("Error: input string have not number elements but it's not a stop-word. Please, input next string")
        return 0, True


stop_word = input("Please, input a stop-word for program: ")
sum_numbers = 0
while True:
    input_str = input("Please, enter numbers separeted by space: ")
    sum_elements, is_continue = sum_input_numbers(input_str, stop_word)
    sum_numbers += sum_elements
    if not is_continue:
        break

print(f"Total sum numbers is: {sum_numbers}")