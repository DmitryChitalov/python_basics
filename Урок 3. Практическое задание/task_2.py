"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""
def get_user(name, surname, year_birthday, city=None, email=None, phone=None):
    user = {
        'name': name,
        'surname': surname,
        'year_birthday': year_birthday,
        'city': city,
        'email': email,
        'phone': phone}
    return user


user = get_user(name='Иван', surname='Иванов', year_birthday=1846, city='Москва', email='i.ivanov@mail.ru', phone='+79115476891')

print(
    f"{user['name']} {user['surname']}"
    f" {user['year_birthday']} года рождения,"
    f" проживает в городе {user['city']},"
    f" email: {user['email']}, телефон: {user['phone']}"
)
"""
for k, v in user.items():
    print(f"{k}: {v}")
"""
