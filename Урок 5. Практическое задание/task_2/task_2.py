"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
+ my_file = open("task2.txt", 'r', encoding='utf-8')
+ content = 0
+ a = -1
+ my_list = []
+       content = my_file.readline()
+       a += 1
+       b = content.split(" ")
+       my_list.append(b)
+ my_list = len(sum(my_list, []))-1
+ print(f'кол-во строк: {a}\nкол-во слов: {my_list}')
+  my_file.close() 
