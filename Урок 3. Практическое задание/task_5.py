"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
    выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
    нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
    вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
    символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
    ранее сумме и после этого завершить программу.
"""


def search_simbol(lst):
    """
    Функция возврата суммы чисел в массиве
    --------------------------------------
    return_mod - условие возврата работы цикла
    1 - продолжает запрос чисел
    2 - останавливает цикл
    """
    return_mod = 1
    sum_nmbs = 0

    for elem in lst:
        if elem == str(elem):
            print(elem)
            sum_nmbs += 0
            return_mod = 2
            break
        else:
            sum_nmbs += elem

    return sum_nmbs, return_mod


all_sum = 0
count_in = 0
print("Ну что... давай будем играть в очередную чудо игру с числами )))\n")
print("Условия простые - вводишь только ЦЕЛЫЕ числа через пробел и нажать Enter")
while True:
    user_nums = ' '
    lst_for_func = []
    print('Если захочешь остановиться - введи любой спецсимвол "!, @, #, $, %, ^, &, *" и нажми Enter!')
    while True:
        user_nums = input("Введите ЦЕЛЫЕ числа через пробел и нажать Enter: ")
        if user_nums != '':
            break
    for elem in user_nums.split(' '):
        try:
            lst_for_func.append(int(elem))
            count_in += 1
        except:
            lst_for_func.append(elem)
    all_sum += search_simbol(lst_for_func)[0]
    worker = search_simbol(lst_for_func)[1]
    if worker == 2:
        break

print(f"Всего сложили {count_in} чисел, сумма которых: {all_sum}")
