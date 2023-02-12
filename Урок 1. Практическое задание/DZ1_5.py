profit = int(input("Ваша прибыль: "))
cost = int(input("Ваши издержки "))
if profit == cost:
    print("Ваша фирма работает в 0 ")
elif profit > cost:
    print("Ваша фирма прибыльна")
else:
    print("Ваша фирма убыточна")

