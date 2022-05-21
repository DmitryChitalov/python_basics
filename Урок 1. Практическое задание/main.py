<<<<<<< HEAD
name1 = "Tom"
print(name1)
a = 10
b = 20
print(a, b)
string = input("hello")
print(input)

time = int(input("Введите время в секундах "))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)
print(f"Время в формате чч:мм:сс   {hours} : {minutes} : {seconds}")

n = int(input("Введите число - "))
total = (n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n)))
print("Сумма чисел n + nn + nnn - %d" % total)

n = abs(int(input("Введите целое положительное число ")))
max = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max:
        max = n % 10
    if n > 9:
        continue
    else:
        print("Максимальное цифра в числе ", max)
        break

profit = float(input("Введите выручку фирмы "))
costs = float(input("Введите издержки фирмы "))
if profit > costs:
    print(f"Фирма работает с прибылью. Рентабельность выручки составила {profit / costs:.2f}")
    workers = int(input("Введите количество сотрудников фирмы "))
    print(f"прибыль в расчете на одного сторудника сотавила {profit / workers:.2f}")
elif profit == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")

a = int(input("Введите результаты пробежки первого дня в км "))
b = int(input("Введите общий желаемый результат в км "))
result_days = 1
result_km = a
while result_km < b:
    a = a + 0.1 * a
    result_days += 1
    result_km = result_km + a
print(f"Вы достигнете требуемых показателей на %.d день" % result_days)
=======
name = input("введите ваше имя")
password = int(input("введите ваш пароль"))
age = int(input("введите ваш возраст"))
print()



seconds_in_hour = 3600
seconds_in_minute = 60


seconds = int(input("Enter a number of seconds: "))


hours = seconds // seconds_in_hour
seconds = seconds - (hours * seconds_in_hour)

minutes = seconds // seconds_in_minute
seconds = seconds - (minutes * seconds_in_minute)

print(" {0:.0f} hours, {1:.0f} minutes, {2:.0f} seconds.".format(
    hours, minutes, seconds))


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
>>>>>>> origin/master
