"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
#Не решил, показанное решение с урока разобрал, но оно тоже не работает (ошибок нет, но резульататы неправильные)

user_lines = 0
user_words = 1

with open(r"C:\Users\Serg\Desktop\fff.txt", 'r') as my_file:
    for line in my_file:
        print(line.replace('\n ', ''))
        print(line)
        for n in line:
            if n == " ":
                user_words += 1
            user_lines += 1
            print(f"Слов в строке {user_lines} = {user_words} \n")
            user_words = 1
        print(f"В файле {user_lines} строк")
