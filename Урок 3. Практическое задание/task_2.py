"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""

def print_user(name, l_name, birth, city, email, phone):
    print(f"Пользователь {name} {l_name} {birth}-го года рождения, проживающий в городе {city}, "
          f"имеет  Email {email} и телефон {phone}")


user_template = {
    'name': 'Имя',
    'l_name': 'Фамилия',
    'birth': 'Год рождения',
    'city': 'Город проживания',
    'email': 'Email',
    'phone': 'Телефон'
}
my_user = {}
for key, value in user_template.items():
    input_value = input(f'{value}: ')
    my_user.update({key: input_value})

print_user(**my_user)