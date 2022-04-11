def summa(rez=0):
    my_summa = input("Введите числа через пробел ").split()
    for e in range(len(my_summa)):
        if my_summa[e] != "e":
            rez = rez + int(my_summa[e])
        else:
            break
    print(rez)
    if "e" in my_summa:
        print("выход из программы")
    else:
        summa(rez)


summa()