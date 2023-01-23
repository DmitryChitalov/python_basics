str_1 = [7, 5, 3, 1]
str_2 = int(input('Введите элемент списка: '))
if str_2 > 7:
    str_1.insert(0, str_2)
elif str_2 < 7 and str_2 > 5:
    str_1.insert(1, str_2)
elif str < 5 and str_2 > 3:
    str_1.insert(2, str_2)
elif str_2 < 3 and str_2 > 1:
    str_1.insert(3, str_2)
else:
    str_1.insert(4, str_2)
print(str_1)