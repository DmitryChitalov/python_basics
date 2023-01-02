# Для списка реализовать обмен значений соседних элементов. Значениями обмениваются элементы с индексами 0 и 1,
# 2 и 3 и т. д. При нечётном количестве элементов последний сохранить на своём месте. Для заполнения списка элементов
# нужно использовать функцию input().

print('Вводите значения элементов списка, нажимайте enter, для окончания ввода нажмите enter без ввода '
      'числа')
el_list = int(input('>'))
my_list = []
while True:
    try:
        my_list.append(el_list)
        el_list = int(input('>'))
    except:
        break
length = len(my_list)
for i in range(0, length - 1, 2):
    buf_el = my_list[i]
    my_list[i] = my_list[i+1]
    my_list[i+1] = buf_el
print(my_list)
