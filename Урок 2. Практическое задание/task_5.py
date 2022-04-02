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
print(f"Rating: {rating}")

pos = 0

while True:
    new_rating = input("Enter new rating: ")
    if "stop" == new_rating:
        exit()
    new_rating = int(new_rating)

    for it in rating:
        if it < new_rating:
            rating.insert(pos, new_rating)
            print(f"Entered {new_rating}. Result: {rating}")
            pos = 0
            break
        else:
            pos += 1
            if pos == len(rating):
                rating.append(new_rating)
                print(f"Entered {new_rating}. Result: {rating}")
                pos = 0
                break
