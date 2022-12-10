revenue = int(input("Укажите сумму выручки фирмы: "))
cost = int(input("Укажите размер издержек фирмы: "))
if revenue > cost:
    print("Ваша фирма приносит прибыль")
elif revenue < cost:
    print("Ваша фирма приносит убытки")
else:
    print("Ваша фирма не получает прибыль")