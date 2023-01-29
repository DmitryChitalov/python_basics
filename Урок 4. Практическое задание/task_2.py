'''
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
'''
'''
result_list = []
list = [int(i) for i in input("Введите список чисел: ").split()]
for i in range(1, len(list)):
    if list[i] > list[i-1]:
        (result_list.append(list[i]))
print("Исходный список: ", list)
print("Список, элементы которого больше предыдущего: ", result_list)
'''
#переработка 29.01.23
def new_list(old_list):
    try:
        return [old_list[i] for i in range(1, len(old_list)) if old_list[i] > old_list[i - 1]]
    except TypeError:
        print('Проверьте введенные значения')

def test():
    my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    print(new_list(my_list))

test()