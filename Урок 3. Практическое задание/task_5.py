"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
    выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
    нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
    вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
    символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
    ранее сумме и после этого завершить программу.
"""
print("----------Чтобы прекратить выполнение программы введите ! или @ или # -------------------")
list_1=['!', '@', '#']
sum_all = 0
def func_comparison(list_x, list_y):
    list_z = [0]
    sum = 0
    indicator_1 = None
    for i in range(0, len(list_x)):
        for j in range(0, len(list_y)):
            if list_x[i] == list_y[j]:
                list_z.insert(0, j)
    if len(list_z) == 1:
        list_y = list(map(int, list_y))
        for i in list_y:
            sum += i
    else:
        for i in range(0, list_z[0]):
            sum += int(list_y[i])
            indicator_1 = True
    return sum, indicator_1

indicator_2 = None
sum_1 = 0
while indicator_2 is None:
    list_2 = list(input("Введите числа через пробел: ").split())
    sum_1, indicator_2 = func_comparison(list_1, list_2)
    sum_all += sum_1
    print("Сумма", sum_all)
print("--------------------Конец---------------------", sum_all)
