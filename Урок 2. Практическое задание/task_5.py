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
number_list = [3, 4, 5, 6, 7, 8]
num = int(input("Введите целое число"))
while num != 0:
    for i in range(len(number_list)):
        if number_list[i] == num:
            number_list.insert(i + 1, num)
            break
        elif number_list[0] < num:
            number_list.insert(0, num)
        elif number_list[-1] > num:
            number_list.append(num)
        elif number_list[i] > num and number_list[i + 1] < num:
            number_list.insert((i + 1, num))
        print(f'Результат {number_list}')
        num = int(input("Введите число: "))
