def div(*args):

    try:
        arg1 = int(input("Входные дивиденды"))
        arg2 = int(input("Входной делитель"))
        res = arg1 / arg2
    except ValueError:
        return "Ошибка значения"
    except ZeroDivisionError:
        return "Неверный делитель! Вы не можете использовать ноль в качестве делителя"

    return res

    if arg2 !=0:
        return arg1 / arg2
    else:
        print("Неверное число! Разделитель не может быть нулевым")

        ...

print(f'результат {div()}')

