my_file = open('task2.txt', 'r')
print(my_file)
content = my_file.read()
print(content)
my_file.close()
my_file = open('task2.txt', 'r')
lines = my_file.readlines()
num_lines = len(lines)
num_words = [len(line.split()) for line in lines]

print("Количество строк: ", num_lines)
print("Количество слов в каждой строке: ", num_words)
