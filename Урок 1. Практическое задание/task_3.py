"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
while True:
    n = input("Введите число n: ")
    try:
        n = int(n)
        break
    except ValueError:
        print("Введите целое число")
        continue
array_result = []
for i in range(n):
    if i == 0:
        array_result.append(n)
    else:
        array_result.append(int(str(array_result[i - 1]) + str(n)))
if n != 0:
    print(f"{' + '.join(str(x) for x in array_result)} = {sum(array_result)}")
else:
    print(0)
