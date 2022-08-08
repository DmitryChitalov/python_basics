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
new_rating = int(input('Введите новое значение рейтинга (натуральное число): '))
flag = False
print(f'Исходный список: {rating}')

for i, index in enumerate(rating):
    if index < new_rating:
        rating.insert(i, new_rating)
        print(f'Новое значение {new_rating} вставили на {i} позицию: {rating}')
        flag = True
        break

if not flag:
    rating.append(new_rating)
    print(f'Новое значение {new_rating} добавили в конец списка: {rating}')
