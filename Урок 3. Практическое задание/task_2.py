"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""
def print_user(name, surname, year_of_birth, city_of_residence, email, phone):
    print(f"Пользователь {name} {surname} {year_of_birth} года рождения, проживает в городе {city_of_residence}, "
          f" email: {email} , телефон: {phone}")

user_template = {
    'name': 'Имя',
    'surname': 'Фамилия',
    'year_of_birth': 'Год рождения',
    'city_of_residence': 'Город проживания',
    'email': 'Email',
    'phone': 'Телефон'
}
my_user = {}
for key, value in user_template.items():
    input_value = input(f'{value}: ')
    my_user.update({key: input_value})

print_user(**my_user)