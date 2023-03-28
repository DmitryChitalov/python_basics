"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

file = open('data.txt', 'r')
Lines = file.readlines()

#Lines = ["Beauty is an expression\n", "Change is what keeps the galaxy spinning. It is what makes it beautiful\n", "You are already whole, already complete, already alive in this moment, already beautiful just as you are\n"]

 
count = 0
print("File has {} Line(s)".format(len(Lines)))
for line in Lines:
    count += 1
    words = line.split()
    print("Line{}: {} - has {} Word(s)".format(count, line.strip(),len(words)))
