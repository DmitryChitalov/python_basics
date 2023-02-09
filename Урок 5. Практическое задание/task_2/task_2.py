"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
txt_file = open('stroki.txt', 'r', encoding='utf-8')
text = txt_file.readlines()
q_line = len(text)
print(f'Строк в файле: {q_line}')
counter = 1
for line in text:
    print(f'Количество слов в строке {counter}: {len(line.split())}')
    counter += 1
txt_file.close()
