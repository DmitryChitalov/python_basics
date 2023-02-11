"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""

user, order  = [], 1
name, surname, year_of_birth, city, email, telephone = None, None, None, None, None, None

while True:
    if name is None:
        tmp = input('Введите Имя пользователя: ')
        if not tmp.isalnum():
            print('Вы вели неверное значение. Попробуйте еще раз.')
            continue

        name = tmp

    if surname is None:
        tmp = input('Введите Фамилию пользователя: ')
        if not tmp.isalnum():
            print('Вы вели неверное значение. Попробуйте еще раз.')
            continue

        surname = tmp

    if year_of_birth is None:
        tmp = input('Введите год рождения: ')
        if not tmp.isdigit():
            print('Вы вели неверное значение.  Попробуйте еще раз.')
            continue

        year_of_birth = int(tmp)

    if city is None:
        city= input('Введите город проживания пользователя: ')
        if not tmp.isdigit():
            print('Вы вели неверное значение.  Попробуйте еще раз.')
            continue

        city = int(tmp)

    if email is None:
        email = input('Введите email пользователя: ')
        if not tmp.isdigit():
            print('Вы вели неверное значение.  Попробуйте еще раз.')
            continue

        city = int(tmp)

    telephone = input('Введите телефон пользователя: ')
    if not tmp.isdigit():
        print('Вы вели неверное значение.  Попробуйте еще раз.')
        continue

    telephone= int(tmp)

    user.append((
        order,
        {
            'name': name,
            'surname': surname,
            'year_of_birth': year_of_birth,
            'city': city,
            'email': email,
            'telephone': telephone
        }
    ))

    name, surname, year_of_birth, city, email, telephone = None, None, None, None, None, None
    order += 1

    print(user)

    q = input('Необходимо добавить еще одного пользователя? (Y/N) ')
    if q.lower() == 'y':
        break

analitics = {
    'name': [],
    'surname': [],
    'year_of_birth': [],
    'city': set(),
    'email': [],
    'telephone': []
}

for _, item in user:
    analitics['name'].append(item['Имя'])
    analitics['surname'].append(item['Фамилия'])
    analitics['year_of_birth'].append(item['год рождения'])
    analitics['city'].add(item['проживает в городе:'])
    analitics['email'].add(item['email: '])
    analitics['telephone'].add(item['телефон: '])

print(analitics)
