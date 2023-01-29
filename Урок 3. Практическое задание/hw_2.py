def database(**kwargs):
    print(f"{kwargs['name']} {kwargs['surname']} {kwargs['year']} год рождения, "
          f"проживает в городе {kwargs['city']}, email: {kwargs['email']}, телефон: {kwargs['phone']}")

database(
    name=input('Введите имя: '),
    surname=input('Введите фамилию: '),
    year=input('Введите год рождения: '),
    city=input('Введите город проживания: '),
    email=input('Введите email: '),
    phone=input('Введите номер телефона: ')

)