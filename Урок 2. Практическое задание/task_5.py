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
import sys

rating = [24, 15, 9, 7, 7, 6, 5, 3, 3, 1]

while True:
    try:
        print(f"Рейтинг = {rating}")
        user_rate = int(input("Введите новый рейтинг >>> "))

        current_rate_count = rating.count(user_rate)

        if current_rate_count:
            last_current_id = rating.index(user_rate) + current_rate_count
            rating.insert(last_current_id, user_rate)
        else:
            if user_rate > rating[0]:
                rating.insert(0, user_rate)
            elif user_rate < rating[-1]:
                rating.append(user_rate)
            else:
                for idx, rate in enumerate(rating):
                    if rate < user_rate:
                        rating.insert(idx, user_rate)
                        break

        print(rating)
    except ValueError:
        print("Неверное число")
    except KeyboardInterrupt:
        sys.exit()
