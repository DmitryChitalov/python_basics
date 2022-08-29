# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

seasons_list = ['winter', 'spring', 'summer', 'autumn']
seasons_dict = {"wi": 'winter', "sp": 'spring', "su": 'summer', "au": 'autumn'}
month = int(input("Введите число месяца: "))

if month == 1 or month == 2 or month == 12:
    print(f"list : {seasons_list[0]}")
    print(f"dictionary : {seasons_dict.get('wi')}")

elif month == 3 or month == 4 or month == 5:
    print(seasons_list[1])
    print(f"dictionary : {seasons_dict.get('sp')}")

elif month == 6 or month == 7 or month == 8:
    print(seasons_list[2])
    print(f"dictionary : {seasons_dict.get('su')}")

elif month == 9 or month == 10 or month == 11:
    print(seasons_list[3])
    print(f"dictionary : {seasons_dict.get('au')}")

else:
    print("Месяцев в году всего 12")
