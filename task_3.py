#Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

a = int(input("Введите номер месяца "))

season_list = ['зима', 'весна', 'лето', 'осень']
season_dict = {1 : 'зима1', 2 : 'весна2', 3 : 'лето3', 4 : 'осень4'}

if (a >= 1 and a < 3) or a == 12:
    print(season_list[0])
    print(season_dict.get(1))
elif a >= 3 and a <= 5:
    print(season_list[1])
    print(season_dict.get(2))
elif a >=6 and a <= 8:
    print(season_list[2])
    print(season_dict.get(3))
elif a >= 9 and a <= 11:
    print(season_list[3])
    print(season_dict.get(4))
elif a <= 0 or a > 12:
    print ("Введено некорректное число. Введите целое число с 1 по 12")
