"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
def two_max(a, b, c):
    numb = [a, b, c]
    summ = []
    numb.sort()
    summ.append(numb[1])
    summ.append(numb[2])
    print(numb[1]+numb[2])
one = int(input('Enter 1st number: '))
two = int(input('Enter 2nd number: '))
three = int(input('Enter 3rd number: '))
two_max(one, two, three)


def maxx(a, b, c):
    my_list = [a, b, c]
    my_list.remove(min(my_list))
    print(my_list[0]+my_list[1])
one = int(input('Enter 1st number: '))
two = int(input('Enter 2nd number: '))
three = int(input('Enter 3rd number: '))
maxx(one, two, three)

