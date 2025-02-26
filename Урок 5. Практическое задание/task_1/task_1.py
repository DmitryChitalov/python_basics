"""
Задание 1. Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна
запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь
вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
сообщать ему об ошибке и снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
"""


def math_operation():  
    operators = {"+", "-", "*", "/"}
    
    operation = input("\nВведите операцию (+, -, *, / или 0 для выхода): ")
    
    if operation in operators:
        try:  
            number01 = int(input("Введите первое число: "))
            number02 = int(input("Введите второе число: "))
        
        except ValueError:
            print("Вы ввели не число, попробуйте еще раз")
            math_operation()
    
        else:
            match operation:  
                case "+":
                    summ(number01, number02)
                    math_operation()
                case "-":
                    diff(number01, number02)
                    math_operation()
                case "*":
                    multi(number01, number02)
                    math_operation()
                case "/":
                    div(number01, number02)
                    math_operation()
    
    elif operation == "0":
        print("Выход")
        return
    
    else:
        print("Введен неверный оператор, попробуйте еще раз")
        math_operation()


def summ(num01, num02):
    print("сумма равна {}".format(num01 + num02))


def diff(num01, num02):
    print("разность равна {}".format(num01 - num02))


def multi(num01, num02):
    print("произведение равно {}".format(num01 * num02))


def div(num01, num02):
    if num02:
        print("деление равно {}".format(num01 / num02))
    else:
        print("На 0 делить нельзя, попробуйте еще раз")


math_operation()
