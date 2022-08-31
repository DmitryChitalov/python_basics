"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
task2 = open('task_2.txt', 'r', encoding="utf-8")
text = task2.readlines()
print(f'Количество строк: {len(text)}')
words = 0
for el in text:
    word = len(el.split(' '))
    words += word
print(f'Количество слов: {words}')
task2.close()