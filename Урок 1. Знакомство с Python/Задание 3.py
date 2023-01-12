# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

inp = int(input('Введите число: '))
print(inp + int((str(inp)+str(inp))) + int((str(inp)+str(inp)+str(inp))))

"""
Оптимальный вариант
inp = input('Введите число: ')
print(int(inp) + int(inp + inp) + int(inp + inp + inp))
"""