"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""
ef person_inf(name,surname,birthday,city,email,phone):
    return f"Name-{name};Surname-{surname}; birthday- {birthday}; city- {city};"\
f"email- {email}; phone -{phone}"
print(person_inf(name='ANN', surname= 'Dark', birthday= '23.08.2003', city= 'Holluwood', email='rtyh8765', phone='4568999'))
