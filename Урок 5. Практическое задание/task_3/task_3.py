translater = {'One': 'odin', 'Two': 'dva', 'Three': 'tri', 'Four': 'chetyre'}
my_list = []
result = []
try:
    file_obj = open("test_4_output.txt", 'r')
    for line in file_obj:
        tokens = line.split(" - ")
        print(tokens)
        if tokens[0] in translater:
            word = translater[tokens[0]]
            result.append(word + ' - ' + tokens[1])
    print(result)
except IOError:
    print("Произошла ошибка ввода-вывода!")

try:
    file_input = open("test_4_input.txt", "w")
    file_input.writelines(result)
except IOError:
    print("Произошла ошибка ввода-вывода!")
