profit = int(input("Введите прибыль компании "))
costs = int(input("Введите издержки компании "))

if profit > costs:
    print("Профицит бюджета")
elif profit < costs:
    print("Дефицит бюджета")
elif profit == costs:
    print("Фирма сработала в 0")