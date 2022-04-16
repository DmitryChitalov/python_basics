"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

user_file = input("Enter file name: ")
f = open(user_file, "r")
str_list = f.readlines()

print(f"In {user_file} string amount: {len(str_list)}")
count = 1
for string in str_list:
    print(f"Word amount in string {count} is: {len(string) - 1}")
    count += 1

f.close()
