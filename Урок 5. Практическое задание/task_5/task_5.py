in_line = "5, 6, 6, 5, 2, 1"
rez = 0
with open("text5.txt", "a", encoding='1251') as f:
    f.write(in_line)
with open("text5.txt", "r", encoding='1251') as f2:
    for el in f2:
        i = el.split(", ")
        for el2 in i:
            rez = rez + int(el2)
print(f"Сумма чисел равна - {rez}")
