seconds_in_hour = 3600
seconds_in_minute = 60


seconds = int(input("Enter a number of seconds: "))


hours = seconds // seconds_in_hour
seconds = seconds - (hours * seconds_in_hour)

minutes = seconds // seconds_in_minute
seconds = seconds - (minutes * seconds_in_minute)

print(" {0:.0f} hours, {1:.0f} minutes, {2:.0f} seconds.".format(
    hours, minutes, seconds))



name = input("введите ваше имя")
password = int(input("введите ваш пароль"))
age = int(input("введите ваш возраст"))
print()


n = int(input("Введите число n: "))
temp = str(n)
t1 = temp + temp
t2 = temp + temp + temp
comp = n + int(t1) + int(t2)
print("Результат равен:", comp)

n = int(input("Введите целое положительное число "))
max1 = n % 10
print(max1)
while n >= 1:
    n = n // 10
    print(n)
    if n % 10 > max1:
        print(n)
        print(max1)
        max1 = n % 10
        print(max1)
    elif n > 9:
        pass
print("Максимальное цифра в числе ", max1)


proceeds = int(input('Введите выручку: '))
costs = int(input('Введите издержки: '))
workers = int(input('Введите количество сотрудников: '))
profit = proceeds - costs
rent = profit / proceeds
salary = profit / workers
while True:
    if proceeds > costs:
        print(f'Вы молодцы, продолжайте в том же духе, прибыль: {profit:.2f}')
        print(f'Соотношение прибыли к выручке: {rent:.2f}')
        print(f'Прибыль фирмы в расчете на одного сотрудника: {salary:.2f}')
        break
    elif proceeds < costs:
        print(f'Выручка меньше издержок : {profit:.2f},  нужно поднажать!')
        break
    else:
        print(f'Выручка и издержки одинаковы, прибыль равна {profit:.2f}, удачи!')
        break

a = int(input(2))
b = int(input(3))
c = 1
while a < b:
    a *= 1.1
    c += 1
print(c)