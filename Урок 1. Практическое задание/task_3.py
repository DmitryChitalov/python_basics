"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

n = int(input("Введите целое число : "))
print(str(n)+''+str(n**2)+''+str(n*3))
"""
Пытался сделать проверку, оно работает, но я не понял как отрабатывает цикл, он 4 раза запрашивает одно и тоже число, при этом считает по первому
def getnumber():
    while True:
        n = input("Введите целое число : ")
        #  if n.isdigit(): return n
        if n.isnumeric():  return n


print(getnumber())
nn = int(getnumber()) * int(getnumber())
nnn = int(getnumber()) ** 3
print(int(getnumber()), int(nn), int(nnn))
"""
