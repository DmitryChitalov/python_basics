sum = 0
current = 20

while current < 4:
    if current % 2 == 0:
        sum = sum + current
    current = current + 2

print(sum)