"""
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""
x = int(input("Введите число >>> "))  # ввод числа пользователем
n = str(x)  # перевод введенного значения в строковый тип
a = n + n  # сложение строкого типа, nn
b = n + n + n  # сложение строкого типа, nnn
c = x + int(a) + int(b)  # сложения всех чисел, при этом переменные a и b переводим в численный тип
print(c)  # вывод суммы
