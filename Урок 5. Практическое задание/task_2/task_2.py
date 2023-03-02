"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open('example.txt', 'r') as f:
    line_count = 0
    word_counts = []
    # Прочитать каждую строку в файле
    for line in f:
        line_count += 1
        words = line.split()
        word_count = len(words)
        word_counts.append(word_count)
        print(f"Строка {line_count} содержит {word_count} слов.")

# Вывести общее количество строк и среднее количество слов в строке
print(f"Всего строк: {line_count}")
print(f"Среднее количество слов в строке: {sum(word_counts) / len(word_counts)}")
