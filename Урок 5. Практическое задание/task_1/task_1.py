f = open("text.txt", "w", encoding='1251')
strings = []
while True:
    stroka = input("введите данные или введите Enter для завершения")
    if stroka != '':
        strings.append(stroka + '\n')
    else:
        break
f.writelines(strings)
