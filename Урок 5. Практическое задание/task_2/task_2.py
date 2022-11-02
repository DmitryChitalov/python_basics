"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
out_f = open("text_file2.txt", "w", encoding='utf-8')
str_list = ['stroka_1\n', 'stroka22 dfdfsdf afaf\n', 'stroka333 sadasd adasdasd\n']
out_f.writelines(str_list)
out_f.close()
a = 0
out_f = open("text_file2.txt", "r", encoding='utf-8')
for line in out_f:
    a += 1
print(f'количство строк в файле: {a}')
out_f.close()
out_f = open("text_file2.txt", "r", encoding='utf-8')
b = 0
for line in out_f:
    b += 1
    words = line.split()
    number_of_words = len(words)
    print(f'Количество слов в строке {b}: {number_of_words}')
out_f.close()
