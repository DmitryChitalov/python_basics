"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""

baseLst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def loop(base):
    resultList = []
    prev = base[0]
    for val in base:
        if val > prev:
            resultList.append(val)
        prev = val

    return resultList


def generator(base):
    return [val for index, val in enumerate(base) if index > 0 and val > base[index - 1]]


print(loop(baseLst))
print(generator(baseLst))
