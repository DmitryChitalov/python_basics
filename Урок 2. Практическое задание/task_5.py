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
usr_rating = [7, 5, 3, 3, 2]
print(f"Текущий рейтинг - {usr_rating}")

while True:
    usr_number = input("Введите натуральное целое число: ")

    if not usr_number.isdigit():
        print("Введены некорректные данные. Попробуйте снова: ")
        continue
    else:
        usr_number = int(usr_number)

    for el in range(len(usr_rating)):
        if usr_rating[el] == usr_number:
            usr_rating.insert(el + 1, usr_number)
            break
        elif usr_rating[0] < usr_number:
            usr_rating.insert(0, usr_number)
        elif usr_rating[-1] > usr_number:
            usr_rating.append(usr_number)
        elif usr_rating[el] > usr_number and usr_rating[el + 1] < usr_number:
            usr_rating.insert(el + 1, usr_number)
    print(f"Текущий рейтинг - {usr_rating}")
    usr_request = input("Хотите завершить? Да(y) Иначе, продолжим: ")
    if usr_request.lower() == "y":
        break
