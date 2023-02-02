"""
5. Программа запрашивает у пользователя строку чисел, разделённых пробелом.
 При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
 Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
 Если специальный символ введён после нескольких чисел,
 то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""


def sum_numbers(list_of_numbers):
    sum_result = 0
    for element in list_of_numbers:
        try:
            sum_result += float(element)
        except ValueError:
            continue
    return sum_result


sum_of_numbers = 0

while True:
    string_of_numbers = input("Введите строку чисел, разделенных пробелом. Для завершения введите '#'\n")
    sum_of_numbers += sum_numbers(string_of_numbers.split(' '))
    if sum_of_numbers != 0:
        print(f"Сумма значений элементов {sum_of_numbers}")
    if string_of_numbers.count('#') > 0:
        break
