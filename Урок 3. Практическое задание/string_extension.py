from typing import Tuple


def is_float(value) -> bool:
    """
        Функция, проверяющая что входная строка является десятичным числом

        :param value: входная строка
        :return: результат проверки
    """
    try:
        float(value)
        return True
    except:
        return False



def is_int(value) -> bool:
    """
        Функция, проверяющая что входная строка является целым числом

        :param value: входная строка
        :return: результат проверки
    """
    if value[0] == "-":
        return value[1:].isdigit()
    return value.isdigit()



def to_float_list(value, split_char = " ") -> Tuple[list, bool, str]:
    """
        Функция, конвертирующая входную строку в список чисел, до первого встреченного нечислового элемента

        :param value: входная строка
        :param split_char: символ разделитель между числами
        :return: результирующий список, признак что все элементы были числовыми, первый не числовой элемент
    """
    input_list = value.split(split_char)
    result_list = []
    is_all_float = True
    not_number_element = None
    for element in input_list:
        if is_float(element):
            result_list.append(float(element))
        else:
            not_number_element = element
            is_all_float = False
            break
    
    return result_list, is_all_float, not_number_element