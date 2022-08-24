def my_sum(*args):
    a = 0
    sym = False
    for n in args:
        try:
            a += int(n)
        except ValueError:
            sym = True
    return a, sym


total = 0

while True:
    numbers = input("Введите целые числа через пробел: ").split(' ')
    amount, stop_sym = my_sum(*numbers)
    total += amount
    print(f"Сумма введенных чисел: {total}")

    if stop_sym:
        print(f"Сумма введенных чисел: {total}, подсчёт окончен")
        break
