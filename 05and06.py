#Задание пятое и шестое вместе

Virychka = int(input('Введите выручку фирмы: '))
Izderzka = int(input('Введите издержки фирмы: '))
sotr = int(input('Введите численность сотрудников фирмы: '))
prib = Virychka - Izderzka
if prib > 0:
    print(f'Финансовый результат - прибыль. Ее величина: {prib}')
    print(f'Рентабельность выручки = {prib / Virychka}')
    print(f'Прибыль фирмы в расчете на одного сотрудника = {prib / sotr}')
else:
    print('Финансовый результат - убыток')