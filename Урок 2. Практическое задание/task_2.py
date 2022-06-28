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
<<<<<<< HEAD
string = input("ВВедите данные  ")
symbol = list(string)
N = 0
for el in range(len(symbol) - 1):
    if el is N:
        tmp = symbol[el]
        symbol[el] = symbol[el + 1]
        symbol[el + 1] = tmp
    else:
        N = N + 2
print(symbol)
=======
symbol = input("ВВедите данные  ").split(' ')
# symbol = list(string)
N_1 = 0
N_2 = 1
while len(symbol) > N_2:
    symbol[N_1],symbol[N_2]=symbol[N_2],symbol[N_1]
    N_1+=2
    N_2+=2

print('Результат', *symbol)
>>>>>>> Amendments_Homework#1,2,3
