def fact(number: int):
    temp_result = 1

    if number <= 0:
        yield temp_result

    for x in range(1, number + 1):
        temp_result *= x
        yield temp_result


N = 4

for el in fact(N):
    print(el)