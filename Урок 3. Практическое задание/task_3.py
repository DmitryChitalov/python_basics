"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))


def my_func_sort(x, y, z):
    func_list = [x, y, z]
    func_list.sort(reverse=True)
    max_func_1 = func_list[0]
    max_func_2 = func_list[1]
    return max_func_1, max_func_2


def my_func_not_sort(x, y, z):
    func_list = [x, y, z]
    m = 0
    Sm = 0
    countM = 0
    countSm = 0
    indM = 0
    for i in func_list:
        if i > m:
            m = i
            indM = countM
        countM += 1
    for i in func_list:
        if i > Sm and countSm != indM:
            Sm = i
        countSm += 1
    return m, Sm

print(my_func_sort(a, b, c))
print(my_func_not_sort(a, b, c))