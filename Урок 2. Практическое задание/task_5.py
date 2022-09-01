"""
5. Реализовать структуру «Рейтинг», представляющую собой не
возрастающий набор натуральных чисел
(каждый элемент ряда меньше или равен предыдущему).

У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.

Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.

Набор натуральных чисел можно задать непосредственно в коде,
например, my_list = [7, 5, 3, 3, 2].
"""
list_1 = [7, 5, 3, 3, 2]
while True:
    print(f'Для завершения программы введите пробел')
    el = input("Введите число: ")
    if el == ' ':
        print(f'Результат: {list_1}')
        exit(0)
    n = int(el)
    j = 0
    result = False
    for item in list_1:
        if n > item:
            list_1.insert(j, n)
            result = True
        j += 1
        if result:
            break
    if not result:
        list_1.append(n)
    print(f'Результат: {list_1}')
