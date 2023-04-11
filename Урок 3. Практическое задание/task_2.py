def user(name, lastname, birthday, city, email, phone):
    return print(f'{name} {lastname}, {birthday} года рождения, '
                 f'зарегистрирован в городе: {city}, Email: {email} Телефон: {phone}')
user(
    name=input('Имя: '),
    lastname=input('Фамилия: '),
    birthday=input('Год Рождения: '),
    city=input('Регистриация: '),
    email=input('email: '),
    phone=input('phone: '),
)
