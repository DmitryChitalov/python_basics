"""
2) Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

my_f = open("Task2.txt", "w", encoding='utf-8')
str_list = [
     "Caro m'è 'l sonno, e più l'esser di sasso,\n",
     "mentre che 'l danno e la vergogna dura;\n",
     "non veder, non sentir m'è gran ventura;\n",
     "però non mi destar, deh, parla basso.\n"
]

my_f.writelines((str_list))

my_f.close()



my_f = open("Task2.txt", "r", encoding='utf-8')
content = my_f.readlines()
print(len(content))
content2 = list(my_f.read())

my_f.close()