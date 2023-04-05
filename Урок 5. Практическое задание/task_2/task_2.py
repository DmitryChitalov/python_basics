"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

str = 0
words = 1

with open("nata2.txt", "r", encoding='utf-8') as f:
    for line in f:
            for n in line:
                if n == " ":
                    words += 1
            str += 1
            print(f"Количество слов в строке {str} = {words} \n")
    words = 1
    print(f"В файле {str} строк")


