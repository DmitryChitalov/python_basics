x = int(input ("Введите число "))
mx = 0
while x > 0:
    n = x % 10
    if n >= mx:
       mx = n
    x = x // 10
print("Наибольшее число:", mx)
