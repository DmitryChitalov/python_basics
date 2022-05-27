def var_func(var1, var2):
    try:
        return var1 //var2
    except ZeroDivisionError:
        print("Вы пытаетесь разделить на ноль!!!")


var1 = int(input("Введите число:"))
var2 = int(input("Введите число:"))

print(var_func(var1, var2))
