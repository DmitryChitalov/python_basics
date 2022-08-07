"""
Задание 2. Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().

Пример:
Введите целые числа через пробел: 1 2 3 4
Результат: 2 1 4 3

Введите целые числа через пробел: 1 2 3
Результат: 2 1 3
"""
numbers = input('Введите числа через пробел: ')
numbers = numbers.split()
new_numbers = []
count = len(numbers)
if count % 2 == 0:
    for i in range(0, count, 2):
        new_numbers.insert(i, numbers[i+1])
        new_numbers.insert(i + 1, numbers[i])
else:
    for i in range(0, count -2, 2):
        new_numbers.insert(i, numbers[i+1])
        new_numbers.insert(i + 1, numbers[i])
    new_numbers.append(numbers[count-1])
print(new_numbers)