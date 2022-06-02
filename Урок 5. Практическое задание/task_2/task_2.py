"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
mylist = ['mytest\n', 'pythonBasic\n', 'practicaltask\n']
with open("text2.txt", 'w+') as file_obj:
    file_obj.writelines(mylist)
with open("text2.txt") as file_obj:
    lines = 0
    letters = 0
    for line in file_obj:
        lines += line.count("\n")
        letters = len(line)-1
        print(f"{letters} letters in line")
    print(f"String count is {lines}") 