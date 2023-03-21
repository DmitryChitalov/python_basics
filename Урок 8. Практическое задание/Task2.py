"""
2) Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

my_f = open("Task2.txt", "w", encoding='utf-8')
str_list = [
     "Будто в руки взял,\n",
     "Молнию, когда во мраке\n",
     "Ты зажег свечу.\n",
]

my_f.writelines(str_list)
my_f.close()

my_f = open("Task2.txt", "r", encoding='utf-8')
content = my_f.readlines()
str_num = len(content)
print(f"Количество строк равно: {str_num}")
my_f.close()

print(f"Количество слов в каждой строке соотвественно равно:")
with open("Task2.txt", encoding='utf-8') as f_obj:
    for line in f_obj:
        my_str = line.split(" ")
        word_num = len(list(my_str))
        print(word_num, end=' ')
