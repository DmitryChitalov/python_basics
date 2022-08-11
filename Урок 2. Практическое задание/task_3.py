d = (int(input('Please input num form 1 - 12: ')))
my_month = ['Jan - Winter', 'Feb - Winter', 'March - Spring',
            'April - Spring', 'May - Spring', 'June - Summer',
            'July - Summer', 'August - Summer', 'Sept - Fall',
            'Oct - Fall', 'Nov - Fall', 'Dec - Winter']
n_month = list(enumerate(my_month, start=1))
d_month = {n_month[0]: n_month for n_month in n_month}

if d <= 12:
    print(d_month[d])
else:
    print('Only 1 - 12')



