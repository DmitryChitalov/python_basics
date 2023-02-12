n = int(input("Введите число:"))
if n >= 0:
   ns = str(n)
   n2 = ns + ns
   n3 = ns + ns + ns
   amount = n + int(n2) + int(n3)
   print("Сумма равна", amount)
else:
    print("Повторите ввод")
