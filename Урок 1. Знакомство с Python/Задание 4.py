# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

a = int(input('Введите целое положительное число: '))
i = 0
max = 0
g = str(a)
while i < len(g):
    if int(g[i]) > max:
        max = int(g[i])
    i+=1
print(max)





"""
inp = int(input())
g = []
for i in str(inp):
    g.append(i)
print(max(g))
"""