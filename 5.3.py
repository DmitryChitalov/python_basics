with open('task03.txt', 'r', encoding='utf-8') as my_f:
    workers = {}
    for line in my_f:
        name, value = line.split()
        workers[name] = value
        if int(value) < 20000:
            print(f'{name}')