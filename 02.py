

def my_func(**user):
    print(f"\nПользователь: {user['name']} {user['family']}, {user['year']} "
          f"года рождения," f" проживает в городе {user['town']}, email: "
          f"{user['pochta']}, телефон: {user['phone']}")


a = input("Введите имя: ")
b = input("Введите фамилию: ")
c = input("Введите год рождения: ")
d = input("Введите город проживания: ")
e = input("Введите электропочту: ")
f = input("Введите контактный телефон: ")
my_func(name=a, family=b, year=c, town=d, pochta=e, phone=f)