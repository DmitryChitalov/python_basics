"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
i = 0
f_obj = open(r"D:\DevOps\Python\Урок5\test1.txt", "r")

while True: #пока верно
        i = i + 1 #счетчик
        line = f_obj.readline()
        word_count = line.count(" ") + 1
        print({i}, {word_count})
        if not line:
            break
f_obj.close()
