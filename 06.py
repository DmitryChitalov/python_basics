spiski = []
tovar = {'название': '', 'описанине': '', 'цена.за 1 ед': '', 'количество': '', 'ед.измер': ''}
analytics = {'название': [], 'описанине': [], 'цена.за 1 ед': [], 'количество': [], 'ед.измер': []}
num = 0
control = None
line = "-" * 30

while True:
    control = input("Для выхода нажмите '1', для продолжения нажмите '2', для аналитики нажмите '3': ")
    if control == '1':
        break
    elif control == '3':
        if len(spisok) == 0:
            print("Пустая строка")
            continue
        print(f'\tТекущая аналитика\n{line}')
        for key, value in analytics.items():
            value = list(set(value))
            print(f'{key[:25]:>10}: {value}\n{line}')
    elif control == '2':
        num += 1
        spisok = dict(tovar)
        for f in tovar.keys():
            pozic = input(f'Введите позицию "{f}": ')
            spisok[f] = pozic if (f == 'название' or f == 'описание' or f == 'ед.измер') else pozic
            analytics[f].append(pozic)
        spiski.append((num, spisok))
    else:
        print("Неправильный ввод")