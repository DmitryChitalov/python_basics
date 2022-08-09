a = int(input('Please input daily kilometers '))
b = int(input('Please input desired res '))
d = 0
while True:
    a *= 1.1
    d += 1
    if a <= b:
        print(f" {d} Day: {round(a,2)} kilometers")
        continue
    if a >= b:
        print(f" Done!!! {d} Day: {round(a,2)} kilometers")
        break

