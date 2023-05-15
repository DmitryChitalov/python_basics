my_file = open('file04.txt', 'r', encoding='utf-8')
content = my_file.readlines()

summary = 0
names = []

for line in content:
    line_split = line.split()
    summary += float(line_split[1])
    if float(line_split[1]) < 20000.00:
        names.append(line_split[0])
my_file.close()

print('Names:', ', '.join(names))
print('Avg:', summary/len(content))
