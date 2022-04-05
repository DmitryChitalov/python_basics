string = input("Введите предложение")
string = string.split(" ")
i = 0
word = []
number = 1
for l in string:
    word = string[i]
    if len(word) <= 10:
        print(f"{number}  {word}")
        number += 1
        i += 1
    else:
        print(f"{number}  {word [0:10]}")
        number += 1
        i += 1
