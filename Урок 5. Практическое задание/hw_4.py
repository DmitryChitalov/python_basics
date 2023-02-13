dict_int = {"one": "один", "two": "два", "three": "три", "four": "четыре"}

with open("file_4.txt", encoding='utf-8') as f_obj:
    for line in f_obj:
        for key in dict_int.keys():
            line = line.replace(key, dict_int[key])
        print(line)
        with open("file_4.txt", 'a') as f_rus:
            f_rus.write(f'\n {line}')