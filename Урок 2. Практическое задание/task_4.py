input_line = input("Введите слова разделенные пробелом: ")
list01 = input_line.split(' ')
print('my_list ==', list01)

for index, list01_line in enumerate(list01):
    print(index, list01_line[:10])
