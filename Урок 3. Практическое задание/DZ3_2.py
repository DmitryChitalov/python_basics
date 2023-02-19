def profile(my_name, my_sname, my_bday, my_city, my_mail, my_phone):
    print(f'Ваше имя - {my_name}, '
          f'ваша фамилия - {my_sname}, '
          f'ваша дата рождения - {my_bday}, '
          f'ваш город - {my_city}, '
          f'ваш e-mail - {my_mail}, '
          f'ваш телефон - {my_phone}')
my_profile = input('Введите данные о себе (имя, фамилия, дата рождения, город, e-mail, телефон), через пробел: ').split(' ')
print(profile(my_name= my_profile[0], my_sname= my_profile[1], my_bday= my_profile[2], my_city= my_profile[3], my_mail= my_profile[4], my_phone= my_profile[5]))