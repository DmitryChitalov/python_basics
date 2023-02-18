my_month = int(input('Введите порядковый номер месяца: '))

#Вариант через list
season_list = ['зима', 'весна', 'лето', 'осень']
if my_month == 12 or my_month == 1 or my_month == 2:
    print(season_list[0])
elif my_month == 3 or my_month == 4 or my_month == 5:
    print(season_list[1])
elif my_month == 6 or my_month == 7 or my_month == 8:
    print(season_list[2])
elif my_month == 9 or my_month == 10 or my_month == 11:
    print(season_list[3])
else:
    print('Ошибка ввода!')

#Вариант через dict
season_dict = {1: 'зима', 2:'зима', 12: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето', 7: 'лето', 8: 'лето',  9: 'осень', 10: 'осень', 11: 'осень', }
print(season_dict.get(my_month))
