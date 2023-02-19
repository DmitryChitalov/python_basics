"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
"""
rating = []  # список элементов
while True:
    el = int(input("Введите число рейтинга: >>> "))  # ввод элементов
    number = None  # начальный индекс пустой
    for i, num in enumerate(rating):
        if el > num:
            number = i  # после добавления элемента индекс увеличивается
            break
    if number is None:
        rating.append(el)  # добавление элемента в конец списка
    else:
        rating.insert(number, el)  # если элемент больше элемента перед ним, оно помещается вперед
    print(rating)  # вывод получившегося сейчас списка
    q = input("Добавить новый элемент в список (y/n)? ")
    # если надо добавить элемент, цикл продолжается
    if q.lower() == 'n':  # если не надо добавлять, цикл прерывается
        break

print("Рейтинг:\n", rating)  # вывод готового списка "Рейтинг"
