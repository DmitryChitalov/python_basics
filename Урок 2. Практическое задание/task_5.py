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
my_list = [7, 5, 3, 3, 2]

user_input = input('Введите число рейтинга: ')
user_int = int(user_input)

count = 0

for i in my_list:

    if i == user_int:
        index_num = my_list.index(i)
        index_sum = index_num + 1
        my_list.insert(index_sum, user_int)
        break

    elif user_int > max(my_list):
        my_list.insert(0, user_int)
        break

    elif user_int < min(my_list):
        my_list.append(user_int)
        break

    elif user_int < i:

        if user_int > my_list[count + 1]:
            my_list.insert(count + 1, user_int)
            break

    count += 1

print(my_list)
