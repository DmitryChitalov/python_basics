def fact(n):
    num_fact = 1
    for i in range(1, n + 1):
        num_fact *= i
    yield num_fact

inp_num = int(input('Введите число для расчета его факториала: '))
for el in fact(inp_num):
    print(el)