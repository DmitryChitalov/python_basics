start = float(input('Сколько километров ты пробежал сегодня?'))
finish = float(input('Сколько километров надо бегать?'))
null = 1
while start <= finish:
    print(f'{null}-й день надо пробежать: {start} км.')
    start = float('{:.2f}'.format(start + (start / 10)))
    null += 1
start = int(start)
print(f'Итого за {null} дней пробежишь не менее {start} км.')
