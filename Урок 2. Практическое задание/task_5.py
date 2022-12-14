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
while True:
    number = int(input("Введите число: "))
    my_list = [7, 5, 3, 3, 2]
    c = my_list.count(number)
    for el in my_list:
        if c > 0:
            i = my_list.index(number)
            my_list.insert(i, number)
            break
        else:
            if number > el:
                j = my_list.index(el)
                my_list.insert(j, number)
                break
            elif number < my_list[len(my_list) - 1]:
                my_list.append(number)
    print(my_list)
    
    
    
    
#another answer
my_list = [7, 5, 3, 3, 2]
while True:
    n = input("Enter number or q")
    if n != 'q':
        my_list.append(int(n))
        my_list.sort(reverse=True)
        print(my_list)
    else:
        break
