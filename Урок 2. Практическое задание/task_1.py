list01 = [1, 1,35,'string', [1,2,3], (1,2,3), {1,2,3}, {1: 1, 2: 2}, True, None]
print ('press any key: ', end='')
for i in list01:
    input('')
    print (f'"{i}" is: {type(i)}', end='')