def my_func():
    var_1 = float(input('Put number 1: '))
    var_2 = float(input('Put number 2: '))
    while True:
        var_2 = 0
        print('put number not = 0 :')
        var_2 = float(input('Put number 2: '))
        break
    return var_1 / var_2


print(my_func())
