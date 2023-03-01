ex_text = open("DZ5_2.txt", 'r')
my_str = 0
my_char = 0
for line in ex_text:
    my_str += 1
    tmp_char = len(line.split(' '))
    my_char += tmp_char
    print(f'{my_str}-я строка - {tmp_char} слов')
print(f'Всего в документе {my_str} строк и {my_char} слов')
ex_text.close()