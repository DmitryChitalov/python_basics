from itertools import count, cycle


def get_number(start_gen, end_gen):
    """
    Функция итератор, генерирующий целые числа, начиная с указанного
    :param start_gen: Число, с какого числа начинать генерировать список
    :param end_gen: Число, до какого числа генерировать список
    :return: Список целых чисел
    """
    result = []
    for el in count(start_gen):
        if el > end_gen:
            break
        result.append(el)
    return result


def get_number_repeating(lst, number_of_repetitions):
    """
    Функция итератор, повторяющий элементы некоторого списка lst.
    :param lst: Список целых чисел на основании которого будут повторяться значения
    :param number_of_repetitions: Число, количество повторений
    :return: Повторяющийся список целых чисел
    """
    result = []
    counter = 1
    for el in cycle(lst):
        if counter > number_of_repetitions:
            break
        counter += 1
        result.append(el)
    return result
