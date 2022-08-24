"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
# Исправил абс. пути. Даже скопировал решение, но оно неверно считает..

user_lines = 0
user_words = 1

with open("fff.txt", "r", encoding="utf-8") as my_file:
    for line in my_file:
        print(line.replace('\n', ''))
        print(line)
        for n in line:
            if n == " ":
                user_words += 1
            user_lines += 1
            print(f"Слов в строке {user_lines} = {user_words} \n")
            user_words = 1
        print(f"В файле {user_lines} строк")
