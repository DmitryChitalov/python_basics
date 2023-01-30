"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
row_count = 0
words_count = 1

with open("f_2.txt", "r", encoding='utf-8') as f_obj:
    for line in f_obj:
        print(line.replace('\n', ''))
        for n in line:
            if n == " ":
                words_count += 1
        row_count += 1
        print(f"Количество слов в строке {row_count} равно: {words_count}")
    print(f"Общее количество строк: {row_count}")