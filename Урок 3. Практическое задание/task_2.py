"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""
#!/usr/bin/env python3
def user_data_ouput(
        user_name = "Иван",
        user_surname = "Иванов",
        user_b_year = "1971",
        user_c_habitat = "Москва",
        user_email = "ivan.ivanov@gmail.com",
        user_phone = "01005321456"):
    
    return print(f"{user_name} {user_surname} {user_b_year} года рождения, проживает в городе {user_c_habitat}, email: {user_email}, телефон: {user_phone}.")

user_data_ouput()
user_data_ouput(
        user_name = "James",
        user_surname = "Hendrix",
        user_b_year = "1942",
        user_c_habitat = "Seattle",
        user_email = "Jimi.Hendrix@gmail.com",
        user_phone = "271942181970")