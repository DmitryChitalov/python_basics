file01 = open('file02.txt', 'r')
content = file01.readlines()
print('Lines:', len(content))
for i in range(len(content)):
    print(f'line {i+1} - {len(content[i].split())} words')
file01.close()