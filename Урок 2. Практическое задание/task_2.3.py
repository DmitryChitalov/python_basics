my_list = ['зима', 'весна', 'лето', 'осень']
my_dict = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}
my_month = int(input("Введите номер месяца = "))
if 1 <= my_month <= 3:
    print(f"Номер месяца {my_month}. Выбрана {my_list[0]}")
    print(f"Номер месяца {my_month}. Выбрана {my_dict.get(1)}")
elif 4 <= my_month <= 6:
    print(f"Номер месяца {my_month}. Выбрана {my_list[1]}")
    print(f"Номер месяца {my_month}. Выбрана {my_dict.get(2)}")
elif 7 <= my_month <= 9:
    print(f"Номер месяца {my_month}. Выбрана {my_list[2]}")
    print(f"Номер месяца {my_month}. Выбрана {my_dict.get(3)}")
elif 10 <= my_month <= 12:
    print(f"Номер месяца {my_month}. Выбрана {my_list[3]}")
    print(f"Номер месяца {my_month}. Выбрана {my_dict.get(4)}")
else:
    print(f"В году 12 месяцев, вы указали {my_month}")

