# Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму
# наибольших двух аргументов.

print('введите три числа')
el_list = int(input('>'))
my_list = []

while True:
    try:
        my_list.append(el_list)
        el_list = int(input('>'))
    except:
        break

sorted(my_list)


def max_mult(arg_1, arg_2):
    res = arg_1 + arg_2
    return res


res = max_mult(my_list[1], my_list[2])
print(f"Сумма: {res}")
