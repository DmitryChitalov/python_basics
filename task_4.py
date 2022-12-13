new_str = input("Введите несколько слов, разделенных пробелом: ").split()
print(new_str)
for ind, el in enumerate(new_str, 1):
    if len(el) >= 10:
        print(ind, el[0:10])
    else:
        print(ind, el)