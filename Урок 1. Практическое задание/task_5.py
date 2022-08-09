revenue = float(input('Сколько фирма заработала:'))
expenses = float(input('Сколько издержек?'))
if revenue > expenses:
    print(f'Мы в плюсе на {revenue - expenses}')
    profitability = float('{:.2f}'.format((revenue / (revenue - expenses)) * 100))
    print(f'Рентабильность составила : {profitability}%')
    people = int(input('Сколько людей работает на фирме?'))
    prof_peop = float('{:.2f}'.format(profitability / people))
    print(f'На каждого человека в фирме по {prof_peop}%')
elif expenses > revenue:
    print(f'Мы в минусе на {expenses - revenue}')
else:
    print('По ходу вышли в ноль')
    
