"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""


with open("test_file_2.txt", "w+") as test_file:
    lines = []
# Ввод строк
    while True:
        s = input("Введите значение (оставьте строку пустой для фиксации ввода): ")
        if s != '':
            lines.append(s)
        else:
            break
# Дозапись строк в файл
    for i in range(len(lines)):
        if i != len(lines)-1:
            test_file.write(lines[i] + '\n')
        else:
            test_file.write(lines[i])

# Количество строк в файле
    test_file.seek(0)
    lines = test_file.readlines()
    print(f'Кол.-во строк в файле: {len(lines)}')
# Цикл перебора строк и вывода кол.-ва слов
    for i in range(len(lines)):
        words_cnt = len([el for el in lines[i].split(" ") if el != "" and el != '\n'])
        print(f'Количество слов в строке {i+1}: {words_cnt}')



