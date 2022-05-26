"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
    выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
    нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
    вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
    символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
    ранее сумме и после этого завершить программу.
"""

def el_string_sum(string, ind):
    arr = string.split(" ")
    mas = []
    try:
        for el in arr:
            ind = el
            mas.append(int(el))
    except ValueError:
        return sum(mas), ind
    return sum(mas), ind


fin_sum = 0
index = ''
while index != 'q':
    enter = input('input integer through space or "q" for quit: ')
    tmp, index = el_string_sum(enter, index)
    fin_sum += tmp
    print(f'sum = {fin_sum}')