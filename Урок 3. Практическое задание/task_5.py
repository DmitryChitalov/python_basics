def my_sum(line):
    global exit_flag
    list01 = line.split()
    if list01[-1] == 'Q':
        exit_flag = 1
        del list01[-1]
    list01 = map(int, list01)
    return sum(list01)


exit_flag = 0
result = 0


while exit_flag == 0:
    line = input('Input numbers or input Q for exit: ')
    result = result + my_sum(line)
    print('Result:', result)
