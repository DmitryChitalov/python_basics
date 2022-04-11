def dannie(*args):
    return args


name = input("введите имя ")
surname = input("введите фамилию ")
year = input("введите год рождения ")
place = input("введите место рождения ")
email = input("введите email ")
phone = input("введите номер телефона ")
print(*dannie(name, surname, year, place, email, phone))
