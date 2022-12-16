def my_file(name, sname, date, city, email, fnumber):
    '''Выводит одной строкой значения параметров.

    Именные параметры запрашиваются у пользователя.
    '''
    print(f"Имя - {name}, фамилия - {sname}, дата рождения - {date}, город "
          f"проживания - {city}, электронный адрес - {email}, номер телефона -"
          f"{fnumber}")
name = input("Введите ваше имя: ")
sname = input("Введите вашу фамилию: ")
date = input("Введите дату рождения: ")
city = input("Введите город проживания: ")
email = input("Введите электронный адрес: ")
fnumber = input("Введите номер телефона: ")

my_file(name, sname, date, city, email, fnumber)