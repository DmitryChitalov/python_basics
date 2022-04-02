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

integer_list = list()
input_data = input("Enter integers: ")
str_list = input_data.split()

for it in str_list:
    try:
        integer_list.append(int(it))
    except ValueError:
        if ' ' == it:
            continue
        else:
            print(f"Skip {it}: it's not integer.")
            continue
        
print(f"Original list: {integer_list}")

length = len(integer_list)
pos = 0

while True:
    if length - pos == 1 or length == pos:
        break;

    integer_list[pos], integer_list[pos + 1] = integer_list[pos + 1], integer_list[pos]
    pos += 2

print(f"Update list: {integer_list}")
