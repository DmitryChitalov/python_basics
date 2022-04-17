"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
my_file = open("Текст.txt", 'r',encoding='utf-8')
content = 0
a = -1
my_list = []
while content != "":
    content = my_file.readline()
    a += 1
    b = content.split(" ")
    my_list.append(b)
my_list = len(sum(my_list, []))-1
print(f'Кол-во строк: {a}\nКол-во слов: {my_list}')
my_file.close()


