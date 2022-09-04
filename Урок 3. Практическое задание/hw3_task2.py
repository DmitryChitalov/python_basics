def info_func(first_name, second_name, birth_year, city, email, phone_num):
    print(f"{first_name} {second_name} {birth_year} года рождения, проживает в городе {city}, "
          f"email: {email}, контактный телефон: {phone_num}")


info_func(first_name=input(f"Введите свое имя: "),
          second_name=input(f"Введите свою фамилию: "),
          birth_year=input(f"Введите год рождения: "),
          city=input(f"Введите город проживания: "),
          email=input(f"Введите свой email: "),
          phone_num=input(f"Введите номер телефона: "))
