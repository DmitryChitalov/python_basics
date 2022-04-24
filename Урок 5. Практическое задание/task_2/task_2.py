lines = 0
words = 1
with open("text2.txt", "r", encoding='1251') as f:
    for line in f:
        for el in line:
            if el == ' ':
                words += 1
        lines += 1
        print(f"число слов в строке {lines} = {words}")
        print(line)
        words = 1
print(f"Число строк в файле равно - {lines}")
