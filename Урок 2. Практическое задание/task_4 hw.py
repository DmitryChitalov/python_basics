__author__ = 'AndreiM'
__version__ = "1.0 24.03.2023"
print("\n task_4 \n -------- \n")

input_txt = input("Введите слова через пробел: ")
lst = ' '.join(input_txt.split())
txt = []
num = 1
for elem in range(lst.count(' ') + 1):
    txt = lst.split()
    if len(str(txt)) <= 10:
        print(f" {num}. {txt[elem]}")
        num += 1
    else:
        print(f"{num}. {txt[elem] [0:10]}")
        num += 1

"""
Пример:
Введите слова через пробел: раз два три
1. раз
2. два
3. три

Введите слова через пробел: раз перерефрижерированность
1. раз
2. перерефриж
"""