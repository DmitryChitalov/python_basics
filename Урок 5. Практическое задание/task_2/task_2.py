"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open("2.txt", encoding="UTF-8") as f:
    data = [x.split() for x in f]
print(f"Количетво строк - {len(data)}")
for x, y in enumerate(data, start=1):
    print(f"Строка {x} - количество слов {len(y)}")
