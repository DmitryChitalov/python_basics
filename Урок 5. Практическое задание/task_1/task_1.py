file01 = open('file01.txt', 'w')

while True:
    line = input('Input line: ')
    if not line:
        break
    file01.write(line + '\n')

file01.close()

