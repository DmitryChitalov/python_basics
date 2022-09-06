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
user_rating = input('Введите рейтинг: ')
int_user_rating = int(user_rating)
for x in range(5):
    if int_user_rating > my_list[0]:
        my_list.insert(0, int_user_rating)
        break
    elif int_user_rating < my_list[4]:
        my_list.insert(5, int_user_rating)
        break
    elif (int_user_rating < my_list[x] and int_user_rating > my_list[x + 1]):
            my_list.insert(x + 1, int_user_rating)
            break
    elif int_user_rating in my_list:
     my_list.insert(my_list.index(int_user_rating), int_user_rating)
     break
print(my_list)
