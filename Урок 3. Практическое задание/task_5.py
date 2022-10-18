"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
    выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
    нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
    вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
    символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
    ранее сумме и после этого завершить программу.
"""


def search_element_with_sym(str_list, search_sym):
    """
    поиск индекса элемента содержащего символ в списке

    :param str_list: список строк для поиска
    :param search_sym: искомый символ
    :return: индекс элемента списка содержащего символ или -1 если такой
             элемент не найден
    """

    index = 0
    for str_val in str_list:
        if str_val.endswith(search_sym):
            return index
        index += 1

    return -1


def search_symbol_pos(str_val, search_sym):
    """
    поиск позиции символа в строке

    :param str_val: строка для поиска
    :param search_sym: искомый символ
    :return: позиция символа в строке или -1 если символ не найден
    """

    symbols = list(str_val)
    index = 0
    for sym in symbols:
        if sym == search_sym:
            return index
        index += 1
    return -1


def extract_on_left(str_val, search_sym):
    """
    извлечение строки слева до искомого символа
    :param str_val:
    :param search_sym:
    :return:
    """
    pos = search_symbol_pos(str_val, search_sym)
    if pos <= 0:
        return None
    return ''.join(list(str_val)[:pos])


END_SYM = '*'
total = 0
finished = False

while True:
    input_str = input("Ведите числа через пробел "
                      f"({END_SYM} чтобы завершить): ")

    separated = input_str.split(" ")
    end_sym_pos = search_element_with_sym(separated, END_SYM)
    if end_sym_pos >= 0:
        finished = True
        left_sym = extract_on_left(separated[end_sym_pos], END_SYM)
        separated = separated[:end_sym_pos]
        if left_sym is not None:
            separated.append(left_sym)

    if len(separated) > 0:
        numbers = map(float, separated)
        total += sum(numbers)
        print(f"текущая сумма: {total}")

    if finished:
        break
