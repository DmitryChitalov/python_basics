print("Привет, Python!")
""" 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. 
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369."""
a = int(input("Введите целое число: "))
b = (a + (a * 10))
c = (b + (a * 100))
print(a + b + c)
