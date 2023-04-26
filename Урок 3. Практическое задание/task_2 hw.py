__author__ = 'AndreiM'
__version__ = "1.0 25.03.2023"
print("\n task_2 \n -------- \n")

def user_args(name, surname, year, city, email, tel):
    return ' '.join([name, surname, year, "года рождения, проживает в городе", city, ", email:", email, ", телефон:", tel])

print(user_args(name=input('Введите имя: '),
                surname=input('Введите фамилию: '),
                year=input('Введите год рождения: '),
                city=input('Введите город проживания: '),
                email=input('Введите email @: '),
                tel=input('Введите телефон +7: ')))


#Иван Иванов 1846 года рождения, проживает в городе Москва, email: jackie@gmail.com, телефон: 01005321456