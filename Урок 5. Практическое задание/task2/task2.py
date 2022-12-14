my_f = open("task2.txt", "r", encoding='utf-8')
content = my_f.readlines()
my_f.close()
print("Содержимое файла: ", content)
i = len(content)
print(f"Количество строк в файле: {i}".format(i))
for el in range(i):
    j = len(content[el].split())
    print(f"{el + 1}-строка содержит слов: {j}".format(el, j))
