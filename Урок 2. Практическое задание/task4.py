s = input("Введите строку: ").split()
i = 0
while i < len(s):
    if len(s[i]) <= 10:
        print("{i} строка: {s}".format(i=i + 1, s=s[i]))
        i += 1
    else:
        buffer = s[i]
        print("{i} строка: {buffer}".format(i=i + 1, buffer=buffer[:10]))
        i += 1