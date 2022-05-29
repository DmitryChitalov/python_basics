# Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.

my_file = open('dz5_2.txt', 'r')
content = my_file.read()
print(f'Содержимое файла {my_file.name}: \n{content}')
my_file = open('dz5_2.txt', 'r')
content1 = my_file.readlines()
content2 = content.split()
print(f'Количество строк в файле - {len(content1)}')
for i in range(len(content1)):
    print(f'Количество символов {i + 1}-ой строки {len(content1[i]) - 1}')
print(f'Общее количество слов - {len(content2)}')
my_file.close()
