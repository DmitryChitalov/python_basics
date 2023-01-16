num = int(input('Введите трехзначное число: '))
num_max = 0
while num > 0:
    if num_max < num%10:
        num_max = num%10
    num = num//10

print(num_max)
