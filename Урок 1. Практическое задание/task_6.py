n1 = int(input())
n2 = int(input())
k = 1
while True:
    n1 *= 1.1
    k += 1
    if n1 >= n2:
        print(k)
        break
    else:
        continue