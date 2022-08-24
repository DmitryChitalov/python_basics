"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
f = open('test_02.txt', 'r+')
f.truncate()
str_list = ['Создать\n', 'Текстовый файл\n', 'Сохранить в нем несколько строк\n', 'Выполнить подсчет количества строк\n']
f.writelines(str_list)

f = open('test_02.txt')
line_count = 0
for line in f:
    line_count += 1

    flag = 0
    word = 0
    for j in line:
        if j != ' ' and flag == 0:
            word += 1
            flag = 1
        elif j == ' ':
            flag = 0

    print(line, word, 'сл.')

print("Количество строк: ", line_count)
f.close()