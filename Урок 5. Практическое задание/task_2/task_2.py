"""
Задание 2. Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной.
При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены, рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
.
"""


#
def bub_values():
    try:
        number = int(input('Введите число: '))
        return number
    except ValueError:
        print("Ошибка ввода числа. Попробуйте снова ! ")
        return bub_values()


def count_bub(number):
    count_positive = 0
    count_negative = 0
    def poisk_num(quall):
        nonlocal count_negative, count_positive
        if quall < 1:
            return quall
        else:
            if int(quall) % 10 % 2 == 1:
                count_negative += 1
            else:
                count_positive += 1
        return poisk_num(quall / 10)

    poisk_num(number)
    return count_negative, count_positive


count_negative, count_positive = count_bub(bub_values())
print(f'Количество отрицательных чисел = {count_negative}')
print(f'Количество положительных чисел = {count_positive}')
