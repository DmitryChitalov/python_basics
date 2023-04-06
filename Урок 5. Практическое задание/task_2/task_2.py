"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
count_strings = 0
count_words = 1

my_f = open("output_ex2.txt", "r", encoding='utf-8')
for string in my_f:
    string = " ".join(string.split())
    print(string)
    for n in string:
        if n == " ":
            count_words += 1
    count_strings += 1
    print(f"Количество слов в строке {count_strings} - {count_words}")
    count_words = 1
print(f"В файле строк - {count_strings}")
my_f.close()