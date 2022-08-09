revenue = int(input('Сколько фирма заработала:'))
expenses = int(input('Сколько издержек?'))
if revenue > expenses:
    print(f'Мы в плюсе на {revenue - expenses}')
elif expenses > revenue:
    print(f'Мы в минусе на {expenses - revenue}')
else:
    print('По ходу вышли в ноль')
