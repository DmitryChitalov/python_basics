# 5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].
raiting = [7, 5, 3, 3, 2]
print(f"Текущий рейтинг: {raiting}")
while True:
    new_count = int(input("Количество новых элементов рейтинга: "))
    for i in range(1, new_count + 1):
     new_score = input('Введите число: ')
     if not new_score.isdigit():
        print("Введены некорректные данные. Должно быть целое положительное число")
        continue
     else:
        new_score = int(new_score)
     idx = None
     for i, num in enumerate(raiting):
        if new_score > num:
            idx = i
            break
        if idx is None:
           raiting.append(new_score)
        else:
           raiting.insert(idx, new_score)
    print(raiting)
    break
