def my_func(name, surname, year, city, email_box, phone):
    return "".join(["Имя: ", name, "; Фамилия: ", surname, "; Год рождения: ", year, "; Город проживания: ", city, "; Email: ", email_box, "; Номер толефона: ", phone, "."])

name = input("Имя: ")
surname = input("Фамилия: ")
year = input("Год рождения: ")
city = input("Город проживания: ")
email_box = input("Email: ")
phone = input("Номер толефона: ")
print(my_func(name, surname, year, city, email_box, phone))