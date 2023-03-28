"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
    выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
    нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
    вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
    символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
    ранее сумме и после этого завершить программу.
"""


def my_funct(inputted_str, base_list_1):
    condition_1 = True
    my_list = inputted_str.split()
    if inputted_str.find('$') == -1:
        base_list_1.extend(my_list)
    else:
        for el in range(my_list.index('$')):
            base_list_1.append(my_list[el])
        condition_1 = False
    if len(base_list_1) == 0:
        result = "Числа, пригодные для суммирования, не введены"
    else:
        result = 0
        for el1 in base_list_1:
            try:
                result += int(el1)
            except ValueError:
                result = "Ошибка вычислений, введены не только целые числа"
                condition_1 = False
    return result, condition_1, base_list_1


condition = True
base_list = []
print("Введите строки целых чисел, разделенных пробелом. Если хотите завершить, одним из элементов должен быть $")
print("Элементы, введенные после элемента $, не будут просуммированы")
while condition:
    input_str = input("Ввод: ")
    res_var, condition, base_list = my_funct(input_str, base_list)
    print(f"Сумма всех введенных чисел: {res_var}")
