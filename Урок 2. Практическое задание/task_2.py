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
#num = (input('Введите целые числа через пробел'))
#
numbers = int(input('Введите колличество цифр в числе'))
number = []
el = 0
for i in range(numbers):  #перебор по указанному пользователем колличеству цифр
    number.append(input('Введите цифру')) #добавление в список number цифр из диапазона перебора
for i in range(int(len(number)/2)): #перебор в уменьшанном в два раза диапазоне number. /2 для отбрасывания нечетности и использования далее по два элемента
    number[el], number[el+1] = number[el+1], number[el]
    el+=2
print(number)







