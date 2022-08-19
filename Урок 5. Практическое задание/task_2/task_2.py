"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
f = open('lorem_ipsum.txt', 'r', encoding="utf-8")
line_num = 0
words_count = 0
total_words = 0
for line in f:
    line = line.strip("\n")
    words_count = len(line.split())
    line_num += 1
    total_words += words_count
    print(f'Line num: {line_num}; words count: {words_count}; line = {line}')
f.close()
print(f'Total lines: {line_num}; Total words: {total_words}')
"""
Line num: 1; words count: 5; line = Lorem Ipsum is simply dummy
Line num: 2; words count: 7; line = text of the printing and typesetting industry.
Line num: 3; words count: 13; line = Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
Line num: 4; words count: 18; line = when an unknown printer took a galley of type and scrambled it to make a type specimen book.
Line num: 5; words count: 14; line = It has survived not only five centuries, but also the leap into electronic typesetting,
Line num: 6; words count: 3; line = remaining essentially unchanged.
Total lines: 6; Total words: 60
"""
