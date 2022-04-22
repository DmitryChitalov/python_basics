def func():
    try:
        a = int(input("Введите 1 число: "))
        b = int(input("Введите 2 число: "))
        return a / b
    except ValueError:
        return
    except ZeroDivisionError:
        return
print(f"Результат деления - {func()}")
