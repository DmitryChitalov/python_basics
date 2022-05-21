# здесь все задания в одном файле для удобства

# задание №2
n = int(input())
print(f'{n//60//60}:{n//60}:{n%60}')

# задание №3
n = str(input())
summ = 0
for i in range(1, int(n) + 1):
    summ += int(n*i)
print(summ)

# задание №4
n = input()
count = len(str(n)) - 1
big = 0
while count > 0:
    if len(str(n)) <= 1:
        big = int(n)
    #print(type(count), count, type(n[count]), n[count])
    if int(n[count]) > int(big):
        big = n[count]
    count -= 1
print(big)


# задание №5
loss = int(input('Введите издержки: '))
prof = int(input('Введите прибыль: '))
print('выручка больше издержек' if int(input('Введите издержки: ')) < int(input('Введите прибыль: '))else 'издержки больше чем выручка')

# задание №6
loss = int(input('Введите издержки: '))
prof = int(input('Введите прибыль: '))
if loss > prof:
    print('издержки больше чем выручка')
elif prof > loss:
    print('выручка больше издержек')
    rent = prof // int(input('введите количество сотрудников '))
    print(f'прибыль на 1 сотрудника равна {rent}')
else:
    print('выручка равно издержкам')


# задание №7
km = int(input())
b = int(input())
days = 1
while True:
    if km >= b:
        print(days)
        break
    km += 0.1 * km
    days += 1
