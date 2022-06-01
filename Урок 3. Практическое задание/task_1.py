def my_func(x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        return "y is'n be a zero"
    except ValueError:
        return "enter only number"


print(my_func(int(input("Enter x = ")), int(input("Enter y = "))))
