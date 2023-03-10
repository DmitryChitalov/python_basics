class MyTypeErr(Exception):
    def __str__(self):
        return f'Введено не число!'

num_list = []
while True:
    num = input('Введите число, для выхода введите "!": ')
    if num == '!':
        break
    try:
        if not num.isdigit():
            raise MyTypeErr
        num_list.append(int(num))
    except MyTypeErr as err:
        print(err)
print(num_list)




