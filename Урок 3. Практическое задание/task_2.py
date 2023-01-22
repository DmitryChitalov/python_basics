"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456"""
"""
name ='Иван'
    surname ='Иванов'
    year ='1846'
    city ='Москва'
    email ='jackie@gmail.com'
    telephone ='01005321456'
"""
def my_func (name, surname, year, city, email, telephone):
     return ' '.join([name, surname, year, city, email, telephone])
print(my_func(surname = 'Иванов', name = 'Иван', year = '1846', city = 'Москва', email = 'jackie@gmail.com', telephone = '01005321456'))