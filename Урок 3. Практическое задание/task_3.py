def not_my_func(*args):
    rez = sum(sorted(list(args), reverse=True)[:2])
    return rez


def my_func(*args):
    rez = 0
    if args[0] > args[1]:
        rez = rez + args[0]
    else:
        rez = rez + args[1]
    if args[2] > args[1]:
        rez = rez + args[2]
    else:
        if args[2] > args[0]:
            rez = rez + args[2]
        else:
            rez = rez + args[0]
    return rez


a = int(input("введите первый аргумент "))
b = int(input("введите второй аргумент "))
c = int(input("введите третий аргумент "))
print(my_func(a, b, c))
print(not_my_func(a, b, c))
