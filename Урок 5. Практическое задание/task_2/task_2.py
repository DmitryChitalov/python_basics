"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
row_count = 0
word_count_dict = {}


with open("my_file05_02.txt", "r") as my_file:
    for row in my_file:
        row_count += 1
        words = row.split(" ")
        word_count_dict[row_count] = len(words)

for info in word_count_dict.items():
    print(f"В строке {info[0]} содержится {info[1]} слов.")
