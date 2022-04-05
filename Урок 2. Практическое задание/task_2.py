spisok = list(input("введите элементы списка"))
print(spisok)
i = 0
l = 0
while l < int((len(spisok)/2)):
    spisok[i], spisok[i+1] = spisok[i+1], spisok[i]
    l += 1
    i += 2
print(spisok)
