"""
Задание 4.

Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и только арифметические операции.
Не используйте взятие по индексу.

Пример:
Ведите целое положительное число: 123456789
Самая большая цифра в числе: 9
"""
# Задание 4 Подсчет наибольшей цифры в веденном числе
number = int(input("Введите целое положительное число:"))
while len(str(number)) > 0:
    if number < 0:
        print("Введено отрицательное значение числа!")
        break
    elif number < 10:
        print("Введено простое число от 0 до 9")
        break
    elif number < 100:
        index_number_1 = number // 10
        index_number_2 = number - index_number_1 * 10
        print(index_number_1, index_number_2)
        if index_number_1 > index_number_2:
            print("Число максимальное значение {0}".format(index_number_1))
            break
        elif index_number_1 == index_number_2:
            print("Числа равны!")
            break
        else:
            print("Число максимальное значение {0}".format(index_number_2))
            break
    elif number < 1000:
        index_number_1 = number // 100
        index_number_2 = number % 100 // 10
        index_number_3 = number - (index_number_2 * 10 + index_number_1 * 100)
        if index_number_1 > index_number_2:
            if index_number_1 > index_number_3:
                print("Число максимальное значение {0}".format(index_number_1))
                break
        elif index_number_2 > index_number_3:
            print("Число максимальное значение {0}".format(index_number_2))
            break
        else:
            print("Число максимальное значение {0}".format(index_number_3))
            break
    elif number < 10000:
        index_number_1 = number // 1000
        index_number_2 = number % 1000 // 100
        index_number_3 = number % 100 // 10
        index_number_4 = number - (index_number_1 * 1000 + index_number_2 * 100 + index_number_3 * 10)
        print(index_number_1, index_number_2, index_number_3, index_number_4)
        if index_number_1 > index_number_2:
            if index_number_1 > index_number_3:
                if index_number_1 > index_number_4:
                    print("Число максимальное значение {0}".format(index_number_1))
                    break
        elif index_number_2 > index_number_3:
            if index_number_2 > index_number_4:
                print("Число максимальное значение {0}".format(index_number_2))
                break
        elif index_number_3 > index_number_4:
            print("Число максимальное значение {0}".format(index_number_3))
            break
        else:
            print("Число максимальное значение {0}".format(index_number_4))
            break
    elif number < 100000:
        index_number_1 = number // 10000
        index_number_2 = number % 10000 // 1000
        index_number_3 = number % 1000 // 100
        index_number_4 = number % 100 // 10
        index_number_5 = number - (
                    index_number_1 * 10000 + index_number_2 * 1000 + index_number_3 * 100 + index_number_4 * 10)
        if index_number_1 > index_number_2:
            if index_number_1 > index_number_3:
                if index_number_1 > index_number_4:
                    if index_number_1 > index_number_5:
                        print("Число максимальное значение {0}".format(index_number_1))
                        break
        elif index_number_2 > index_number_3:
            if index_number_2 > index_number_4:
                if index_number_2 > index_number_5:
                    print("Число максимальное значение {0}".format(index_number_2))
                    break
        elif index_number_3 > index_number_4:
            if index_number_3 > index_number_5:
                print("Число максимальное значение {0}".format(index_number_3))
                break
        elif index_number_4 > index_number_5:
            print("Число максимальное значение {0}".format(index_number_4))
            break
        else:
            print("Число максимальное значение {0}".format(index_number_5))
            break
    elif number < 1000000:
        index_number_1 = number // 100000
        index_number_2 = number % 100000 // 10000
        index_number_3 = number % 10000 // 1000
        index_number_4 = number % 1000 // 100
        index_number_5 = number % 100 // 10
        index_number_6 = number - (
                    index_number_1 * 100000 + index_number_2 * 10000 + index_number_3 * 1000 + index_number_4 * 100 + index_number_5 * 10)
        if index_number_1 > index_number_2:
            if index_number_1 > index_number_3:
                if index_number_1 > index_number_4:
                    if index_number_1 > index_number_5:
                        if index_number_1 > index_number_6:
                            print("Число максимальное значение {0}".format(index_number_1))
                            break
        elif index_number_2 > index_number_3:
            if index_number_2 > index_number_4:
                if index_number_2 > index_number_5:
                    if index_number_2 > index_number_6:
                        print("Число максимальное значение {0}".format(index_number_2))
                        break
        elif index_number_3 > index_number_4:
            if index_number_3 > index_number_5:
                if index_number_3 > index_number_6:
                    print("Число максимальное значение {0}".format(index_number_3))
                    break
        elif index_number_4 > index_number_5:
            if index_number_4 > index_number_6:
                print("Число максимальное значение {0}".format(index_number_4))
                break
        elif index_number_5 > index_number_6:
            print("Число максимальное значение {0}".format(index_number_5))
        else:
            print("Число максимальное значение {0}".format(index_number_6))
            break
print("Команда выполнена успешно!")