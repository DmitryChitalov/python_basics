# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.# Например, пользователь ввёл число# 3. Считаем 3 + 33 + 333 = 369.print('task_3\n')n = input("Введите число для подсчета: ")nn = int(n + n)nnn = int(n + n + n)n = int(n)result = n + nn + nnnprint(result)