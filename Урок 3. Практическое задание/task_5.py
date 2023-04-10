"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
    выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
    нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
    вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
    символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
    ранее сумме и после этого завершить программу.
"""
result = 0
end_flag = False
error_flag = False


def list_sum(*args):
    """Функция считает сумму подготовленного заранее числового списка"""
    loc_result = 0
    loc_list = list(args[0])
    for el in loc_list:
        loc_result += el
    return loc_result


while (not end_flag) and (not error_flag):
    entered_list = input("Введите числа через пробел, для завершения введите '!': ").split()
    numbers_list = []
    for el in entered_list:
        try:
            numbers_list.append(int(el))
        except ValueError:
            if el == "!":
                end_flag = True
                break
            else:
                error_flag = True
                break
    result += list_sum(numbers_list)
    if error_flag:
        print('Ошибка ввода!!')
        break
    else:
        print(f"Сумма с накоплением: {result}")
