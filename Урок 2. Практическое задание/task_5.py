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

rating = [7, 5, 3, 3, 2]
# первый вариант
num = input('input positive integer or "q" for quit: ')
while num != 'q':  # бесконечный ввод до ввода буквы q
    num = int(num)
    if rating.count(num) == 0:  # если вводимого значения нет в рейтинге
        for el in rating:
            if num > el:
                rating.insert(rating.index(el), num)
                break
            elif num < rating[len(rating) - 1]:
                rating.append(num)
    else:  # если вводимое значение есть в рейтинге
        rating.insert(rating.index(num) + rating.count(num), num)
    print(rating)
    num = input('input positive integer or "q" for quit: ')

# второй вариант
num = input('input positive integer or "q" for quit: ')
while num != 'q':  # бесконечный ввод до ввода буквы q
    rating.append(int(num))
    rating.sort()
    rating.reverse()
    print(rating)
    num = input('input positive integer or "q" for quit: ')

