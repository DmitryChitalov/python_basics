"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
    выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
    нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
    вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
    символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
    ранее сумме и после этого завершить программу.
"""

def my_sum(*args):
    """
    Функция принимает список значений возвращает сумму его элеменов.
    :param args:Список значений
    :return:Сумма элементов списка
    """
    return sum(*args)


def string_to_int_list(input_string):
    """
    Функция конвертирует строку в список чисел
    :param input_string:Строка чисел с пробелами в качестве разделителя
    :return: список чисел
    """
    res_list = [int(i) for i in input_string.split(" ")]
    return res_list


# # Промежуточная проверка
# my_string = "1 2 3 4"
# my_list = string_to_int_list(my_string)
# print(my_sum(my_list))

last_symb = ""
itog_sum = 0

while last_symb != "*":

    imp_string = input("Введите строку чисел через пробел "
                       "(Для завершения цикла введите символ \"*\" в конце или вместо строки ): ")
    last_symb = imp_string[len(imp_string) - 1]

    if last_symb == "*" and len(imp_string) > 1:
        imp_string = imp_string.split("*")[0]
# На случай, если просто введен символ окончания цикла без чисел.
    if last_symb == "*" and len(imp_string) == 1:
        imp_string = "0"

    tmp_list = string_to_int_list(imp_string)
    itog_sum = itog_sum + my_sum(tmp_list)
    print(f"Сумма равна: {itog_sum}")