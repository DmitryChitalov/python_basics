spisok = list(input("введите элементы списка через пробел").split(' '))
print(spisok)
i = 0
l = 1
while l < int(len(spisok)):
    spisok[i], spisok[l] = spisok[l], spisok[i]
    l += 2
    i += 2
print(spisok)
