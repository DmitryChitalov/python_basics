'''
Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
'''


def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])


print(my_func(name='Имя', surname='Фамилия', year='1960', city='Город', email='почта', telephone='7345700987'))
