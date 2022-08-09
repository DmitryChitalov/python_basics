p = int(input('Please type Your profit: '))
c = int(input('Please type Your costs: '))
pl = p - c
pm = pl / p
if p >= c:
    print('Gratulations Your profit = ' f' {pl}')
    print('Your profit margin' f' {pm}')
    emp = input('Please input count of Your full time employees or type 0 if You want to close the app ')
    if int(emp) > 0:
        print('Your profit per employee: ' f'{p / int(emp)}')
    else:
        print('Have a good day')

if p < c:
    print('Your lost = ' f' {pl * -1}' '  You need to work more time')
    emp = input('Please input count of Your full time employees or type 0 if You want to close the app ')
    if int(emp) > 0:
        print('Your profit per employee: ' f'{p / int(emp)}')
    else:
        print('Have a good day')
