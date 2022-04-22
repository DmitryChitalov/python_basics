def func():
        first_name = input("Введите имя: ")
        last_name = input("Введите фамилию: ")
        born_year = input("Введите год рождения: ")
        address = input("Введите город проживания: ")
        email = input("Введите email: ")
        phone = input("Введите номер телефона: ")
        return (f"Имя: {first_name} Фамилия: {last_name} Год рождения: {born_year} "
              f"Город проживания: {address} email: {email} Телефон: {phone}")
print(func())
