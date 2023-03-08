# 2. Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

count_element = int(input("Введите количество элементов списка "))
list_2 = []
i = 0
element = 0
while i < count_element:
    list_2.append(input("Введите значение "))
    i += 1
for elem in range(int(len(list_2)/2)):
        list_2[element], list_2[element + 1] = list_2[element + 1], list_2[element]
        element += 2
print(list_2)
