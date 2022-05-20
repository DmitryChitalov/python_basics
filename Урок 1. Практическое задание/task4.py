s    = input("Введите цело положительной число: ")
try:
    int(s)
except ValueError:
    print("ОШИБКА: ЧИСЛО СОДЕРЖИТ СИМВОЛ!")
    quit()
max_ = 0
if (len(s) > 0):
    max_ = int(s[0])
    i    = 1
    len_ = len(s)
    while (i < len_):
        s_ = int(s[i])
        if (max_ < s_):
            max_ = s_
        i += 1
print(f"Самая большая цифра в числе {s} это {max_}")
