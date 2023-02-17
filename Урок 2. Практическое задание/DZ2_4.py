my_list = list(input('Введите слова через пробел: ').split(' '))
for index, value in enumerate(my_list, 1):
        print(f'{index}. {value [:10]}')



