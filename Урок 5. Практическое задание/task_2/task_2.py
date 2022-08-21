"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
my_f = open("task2.txt", encoding='utf-8')
content = my_f.readlines()
str_count = 0
my_f.close()
for i in content:
    str_count = str_count + len(i.split())

print(f"Количество строк: {len(content)}")
print(f"Количество слов: {str_count}")
