# tack_5

plus = int(input('Введите значение прибыли: '))
minus = int(input('Введите значение издержек: '))
people = int(input('Ввдите количество работников: '))

if plus > minus:
    print('Выручка больше издержек')
    clear_plus = plus - minus
    rent = clear_plus / plus
    print('Рентабельность {} выручки {}: {:.2f}'.format('нашей', 'составила',
                                                        rent))
    clear_for_person = float(clear_plus / people)
    print(
        'Прибыль фирмы в расчете на одного сотрудника: %s' % clear_for_person)
else:
    print('Фирма работает в убыток')
