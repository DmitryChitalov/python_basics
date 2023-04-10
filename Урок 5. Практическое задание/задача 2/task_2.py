"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
f = open("file.txt", "r")
content = f.read()
f.close()

rows = content.split("\n")
print("Total rows count: " + str(len(rows)))

for index, row in enumerate(rows):
    print(f"Row {index + 1} has {len(row.split())} words")
