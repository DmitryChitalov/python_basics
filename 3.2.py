def main(first_name: str = None,
         last_name: str = None,
         year: int = None,
         city: str = None,
         phone: str = None,
         email: str = None):
    return f"{first_name} {last_name} ({year}), {city}, {phone}, {email}"


# def main(**kwargs):
#     return f"{kwargs['first_name']} {kwargs['last_name']} ({kwargs['year']}), {kwargs['city']}, {kwargs['phone']}, {kwargs['email']}"


user_first_name = input("Имя >>> ")
user_last_name = input("Фамилия >>> ")
user_year = int(input("Год рождения >>> "))
user_city = input("Город >>> ")
user_email = input("Email >>> ")
user_phone = input("Номер телефона >>> ")

print(
    main(first_name=user_first_name, last_name=user_last_name,
         year=user_year, city=user_city, email=user_email,
         phone=user_phone)
)
