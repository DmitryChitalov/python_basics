number = int(input("Введите кол-во элементов списка: "))
i = 0
j = 0
print("Введите элементы списка: ")
s = []
while i < number:
    s.append(input())
    i += 1
if (number % 2) == 0:
    while j < number:
        buffer = s[j]
        s[j] = s[j + 1]
        s[j + 1] = buffer
        j += 2
else:
    while j < number - 1:
        buffer = s[j]
        s[j] = s[j + 1]
        s[j + 1] = buffer
        j += 2

print(s)
