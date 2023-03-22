# 2. Создать текстовый файл (не программно),
# сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.\
my_f = open('C:/Users/Viktoria/Desktop/task_2.txt', 'r')
content = my_f.read()

my_f = open('C:/Users/Viktoria/Desktop/task_2.txt', 'r', encoding='utf-8')
content = my_f.readlines()
print(f'Количество строк в файле - {len(content)}')

my_f = open('C:/Users/Viktoria/Desktop/task_2.txt', 'r', encoding='utf-8')
my_f = my_f.readlines()
for i in range(len(content)):
    content = my_f[i].split()
    print(f'В {i + 1}-ой строке {len(content)} слов(а)')
