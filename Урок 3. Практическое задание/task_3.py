"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
def my_func(a, b, c):
    my_numbers = [a, b, c]
    my_numbers.sort()
    print(f"Cумма наибольших двух аргументов c sort(): {my_numbers[1] + my_numbers[2]}")

def my_func_nosort(a, b, c):
    my_numbers = [a, b, c]
    for i in range(len(my_numbers)):
        for j in range(i + 1, len(my_numbers)):
            if my_numbers[i] > my_numbers[j]:
                my_numbers[i], my_numbers[j] = my_numbers[j], my_numbers[i]
    print(f"Cумма наибольших двух аргументов без sort(): {my_numbers[1] + my_numbers[2]}")

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
my_func(a, b, c)
my_func_nosort(a, b, c)




