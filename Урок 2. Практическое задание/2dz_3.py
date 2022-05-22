# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.

my_list = ['зима', 'весна', 'лето', 'осень']
my_dict = {0: 'зима', 1: 'весна', 2: 'лето', 3: 'осень'}
month = int(input("Введите месяц по номеру: "))
if month == 1 or month == 12 or month == 2:
    print(my_dict.get(0))
    print(my_list[0])
elif month == 3 or month == 4 or month == 5:
    print(my_dict.get(1))
    print(my_list[1])
elif month == 6 or month == 7 or month == 8:
    print(my_dict.get(2))
    print(my_list[2])
elif month == 9 or month == 10 or month == 11:
    print(my_dict.get(3))
    print(my_list[3])
else:
    print("Такого месяца не существует")
