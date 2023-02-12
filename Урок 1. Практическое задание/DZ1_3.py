n = int(input("Введите число:"))
if n >= 0:
   ns = str(n)
   n2 = ns + ns
   n3 = ns + ns + ns
   sum = n + int(n2) + int(n3)
   print("Сумма равна", sum)
else:
    print("Повторите ввод")
