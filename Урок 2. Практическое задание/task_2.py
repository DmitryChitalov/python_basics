"""
2. Для списка реализовать обмен значений соседних элементов.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
При нечётном количестве элементов последний сохранить на своём месте.
Для заполнения списка элементов нужно использовать функцию input().
"""

list_length = int(input("введите длинну списка :"))
list_different_types_data = []
for index in range(list_length):
    list_different_types_data.append(int(input("введите элемент списка: ")))
print(list_different_types_data)
if list_length % 2 == 0:
    for index in range(0, list_length, 2):
        buffer_var = list_different_types_data[index]
        list_different_types_data[index] = list_different_types_data[index + 1]
        list_different_types_data[index + 1] = buffer_var
else:
    for index in range(0, list_length - 1, 2):
        buffer_var = list_different_types_data[index]
        list_different_types_data[index] = list_different_types_data[index + 1]
        list_different_types_data[index + 1] = buffer_var
print(list_different_types_data)
