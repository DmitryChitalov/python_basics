f_obj = open("file_1.txt", 'w', encoding='utf-8')
lines = []
while True:
    line = input('Введите новые данные или нажмие ENTER для завершения ввода: ')
    if line != '':
        lines.append(line + '\n')
    else:
        break
f_obj.writelines(lines)

with open("file_1.txt", 'r', encoding='utf-8') as f_obj:
    content = f_obj.readlines()
    print(content)

with open("file_1.txt", 'r', encoding='utf-8') as f_obj:
    for line in f_obj:
        print(line)