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

user_val = int(input("Введите натуральное число: "))


# Вариант 1


init_rating = [7, 7, 7, 5, 3, 3, 2]

rating = init_rating.copy()
rating.append(user_val)

sorted_rating = sorted(rating, reverse=True)

print(f"Пользователь ввел число {user_val}. ", end='')
print(f"Результат: {', '.join([str(i) for i in sorted_rating])}.")

# Вариант 1

init_rating = {7: 3, 5: 1, 3: 2, 2: 1}

rating = init_rating.copy()
num_of_entries = rating.get(user_val)

if num_of_entries is None:
    rating.update({user_val: 1})
else:
    rating[user_val] += 1

print(f"Пользователь ввел число {user_val}. Результат: ", end='')
sorted_rating = sorted(rating, reverse=True)
last_key = sorted_rating[len(sorted_rating) - 1]
for key in sorted_rating:
    count_values = rating[key]
    for index in range(count_values):
        print(f"{key}{', ' if index < count_values - 1 else ''}", end='')
    print(", " if key != last_key else ".", end='')
print()
