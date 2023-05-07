def user_data_to_string(name, surname, year, city, email, phone):
    return ', '.join([name, surname, year, city, email, phone])


result = user_data_to_string(name='Artur', surname='Morozov', year='1988',
                            city='Kazan', email='Artur_1.0@mail.ru', phone='89274253820')

print(result)
