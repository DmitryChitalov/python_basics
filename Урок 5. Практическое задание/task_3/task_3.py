replace_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

my_file = open('file03.txt', 'r', encoding='utf-8')
new_file = open('file03_new.txt', 'w', encoding='utf-8')

for line in my_file:
    line = line.split(' - ')
    line[0] = replace_dict[line[0]]
    line = ' - '.join(line)
    new_file.write(line)

my_file.close()
new_file.close()