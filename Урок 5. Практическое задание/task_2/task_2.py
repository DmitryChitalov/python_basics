"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
file_u = open("filedata.txt", "r")
x = 0
for line in file_u:
    x += 1
    print(line)
    y = 0
    for i in line:
        y += 1
    print(f" количество символов в строке ", {y})
print(f" количество строк в файле ", {x})
file_u.close()
