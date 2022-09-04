my_f = open("numbers.txt", "w", encoding='utf-8')
my_f.write("1 2 3 4 5 6 7 8 9 10")
my_f.close()

with open("numbers.txt", "r", encoding='utf-8') as f_obj:
    for line in f_obj:
        line = line.split(' ')
        print(line)
        sum_num = sum(map(int, line))
        print(sum_num)
