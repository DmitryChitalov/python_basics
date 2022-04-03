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

rate = []
try:
    while True:
        rate.append(int(input("Input your rate number or any string for stop: ")))
except:
    rate.sort(reverse=True)
    print(f"Base rate is {rate}")
    
    try:
        while True:
            user_rate = int(input("Input your rate number or any string for stop: "))
            if len(rate) == 0:
                rate.append(user_rate)
            else:
                index = 0
                while user_rate <= rate[index] and index < len(rate) - 1:
                    index += 1
                
                print(f"Add rate in index {index}")
                rate.insert(index, user_rate)

            print(f"Updated rate is {rate}")
    except:
        print(f"Total rate is {rate}")