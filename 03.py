def my_func(var1,var2,var3):
    print(f'Сумма двух наибольших элементов:'
          f'{var1 + var2 + var3 - min([var1,var2,var3])}')

my_func(
    int(input("First:")),
    int(input('second:')),
    int(input("third:")))
