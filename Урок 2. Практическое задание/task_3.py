"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""
your_month = int(input("Введите номер месяца от 1 до 12, чтобы узнать сезон"))
season_list = ['зима', 'весна', 'лето', 'осень']
season_dict = {1 : 'зима', 2 : 'весна', 3 : 'лето', 4 : 'осень'}
while True:
    if your_month >= 3 and your_month <= 5 :
        print(f"Введенный номер месяца в списке это {season_list[1]}")
        print(f"Введенный номер месяца в справочнике это {season_dict.get(2)}")
        break
    elif your_month >= 6 and your_month <= 8 :
        print(f"Введенный номер месяца в списке это {season_list[2]}")
        print(f"Введенный номер месяца в справочнике это {season_dict.get(3)}")
        break
    elif your_month >= 9 and your_month <= 11 :
        print(f"Введенный номер месяца в списке это {season_list[3]}")
        print(f"Введенный номер месяца в справочнике это {season_dict.get(4)}")
        break
    elif your_month == 12 or your_month < 3 :
        print(f"Введенный номер месяца в списке это {season_list[0]}")
        print(f"Введенный номер месяца в справочнике это {season_dict.get(1)}")
        break



