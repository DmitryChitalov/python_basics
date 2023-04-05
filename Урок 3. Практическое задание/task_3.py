"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
# Вариант 1, sort.
def dif_sum(a, b, c):
    my_sum = [a, b, c, ]
    my_sum.sort()
    my_sum.pop(0)
    return sum(my_sum)


res = dif_sum(a=int(input('Введите первое значение: ')),
              b=int(input('Введите второе значение: ')),
              c=int(input('Введите третье значение: ')))
print(res)


# Вариант 2, без использования sort
def dif_summ():
    try:
        a = int(input('Введите первое значение: '))
        b = int(input('Введите второе значение: '))
        c = int(input('Введите третье значение: '))
        my_summ = [a, b, c, ]
        my_summ.remove(min(a, b, c))
        return sum(my_summ)
    except ValueError:
        return 'Необходимо ввести число, запустите программу ещё раз.'


res = dif_summ()
print(res)
