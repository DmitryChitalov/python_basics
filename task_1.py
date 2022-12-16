def my_division(var_1, var_2):
    ''' Возвращает результат деления с остатком

    Позиционные параметры запрашиваются у пользователя.
    Предусмотрено исключение в случае деления на ноль.
    '''
    try:
        return var_1 / var_2
    except ZeroDivisionError:
        return
var_1 = int(input("Введите первое число: "))
var_2 = int(input("Введите второе число: "))
print(my_division(var_1, var_2))