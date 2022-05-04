def generator_file():
    f_file_open = open('2.txt', 'w')
    data_list = [
                'One', 'Two', 'Three', 'Four', 'Five',
                ]
    data = [
        f_file_open.write(str(data_list[i]) + "\n") for i in range(len(data_list))
    ]
    f_file_open.close()
generator_file()
def count():
    file_open = open('2.txt', 'r')
    print("Количество строк: " + str(len(file_open.readlines())) + ".")
    file_open = open('2.txt', 'r')
    print("Количество элементов: " + str(len(file_open.read())) + ".")
count()
