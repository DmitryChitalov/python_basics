x = print("Какое у Вас значение прибыли?")
x1 = int(input())
y = print("А какое у Вас значение издержек?")
y1 = int(input())


if (x1>y1) :
    print("Ваша компания прибыльна")

if (y1>x1) :
    print("Ваша компания работает в убыток")

q = print("Какая у вас выручка?")
q1 = int(input())
q2 = (x1/q1)
print('ваша рентабельность выручки составила' +q2)

a = print("Какая численность сотрудников у вас работает?")
a1 = int(input())
a2 = x1/a1
print("Прибыль фирмы в расчете на 1 сотрудника" + a2)


