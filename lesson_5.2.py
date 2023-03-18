"""
2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
выполнить подсчёт строк и слов в каждой строке.
"""

my_file = open('5.2.txt', 'r', encoding='utf-8')
line = 0
for i in my_file:
    line += 1
    flag = 0
    word = 0
    for j in i:
        if j != ' ' and flag == 0:
            word += 1
            flag = 1
        elif j == ' ':
            flag = 0
    print(i, len(i), 'симв.', word, 'сл.')
print(line, 'стр.')
my_file.close()
