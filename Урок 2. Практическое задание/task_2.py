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

list = (input("Please enter space-separated values:")).split(" ")
number_of_items = len(list)


if number_of_items % 2 != 0:                # Check if number of items in the list is even
    number_of_items = number_of_items-1     # And if not - make it even by substracting 1


for i in range(1,number_of_items,2):        # Create a range of indexes to be processed
         
    index_odd = i                           # Take a record of odd index (e.g. 1,3,5 etc.)
    index_even = i - 1                      # Find it's neighbour index to the left
    number1 = list[index_even]              # Find number in the list by index1
    number2 = list[index_odd]               # Find number in the list by index2

    list[index_even] = number2              # Assign new value to the odd index
    list[index_odd] = number1               # Assign new value to it's neighbour to the left

print(list)