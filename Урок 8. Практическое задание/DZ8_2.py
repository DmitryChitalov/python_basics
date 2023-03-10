class ErrDiv(Exception):

    def __str__(self):
        return f'Ошибка! Делить на ноль нельзя!'

my_num = input('Введите делимое / делитель ').split('/')
divisible = int(my_num[0])
divider = int(my_num[1])

try:
    if divider == 0:
        raise ErrDiv
    else:
        res = divisible / divider
except ValueError:
    print('Ошибка! Введите числа')

print(f'Частное равно: {res} ')
