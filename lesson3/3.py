#Реализовать функцию my_func(), которая принимает три позиционных аргумента,
#и возвращает сумму наибольших двух аргументов.
#Попробуйте решить задачу двумя способами:
#1) используя функцию sort()
#2) без функции sort()

numb1 = int(input("Введите первое число: "))
numb2 = int(input("Введите второе число: "))
numb3 = int(input("Введите третье число: "))

my_func = [numb1, numb2, numb3]
print(sum(sorted(my_func)[1:]))


def my_func(numb1, numb2, numb3):
    if numb1 >= numb2 and numb2 >= numb3:
        return numb1 + numb2
    elif numb1 > numb2 and numb1 < numb3:
        return numb1 + numb3
    else:
        return numb1 + numb3

print(f'Ответ: - {my_func(int(input("Введите первое число: ")), int(input("Введите второе число: ")), int(input("Введите третье число: ")))}')