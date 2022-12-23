"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
    выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
    нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
    вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
    символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
    ранее сумме и после этого завершить программу.
"""
def my_sum(my_list):
    s_sum = 0
    for item in my_list:
        try:
            s_sum += float(item)
        except ValueError:
            continue
    return s_sum


def sum_my_string(s):
    s = s.replace('#', '')
    s = s.replace(',', '.')
    numbers = s.split(' ')
    return my_sum(numbers)


numbers_sum = 0
while True:
    numbers_sting = input("Введите строку чисел, разделенных пробелом. Для завершения введите символ '#'\n")
    numbers_sum += sum_my_string(numbers_sting)
    if numbers_sum != 0:
        print(f"Сумма значений элементов {numbers_sum}")
    if numbers_sting.count('#') > 0:
        break
