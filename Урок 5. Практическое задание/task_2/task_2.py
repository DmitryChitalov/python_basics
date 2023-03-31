"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
line_cnt = 0
word_cnt = 0

with open("in_file.txt") as file_obj:
    for line in file_obj:
        line_cnt += 1
        word_cnt += len(line.split())
        print(f"Количество слов в строке {line_cnt}: {len(line.split())}")

print(f"Общее количество строк: {line_cnt}")
print(f"Общее количество слов: {word_cnt}")
