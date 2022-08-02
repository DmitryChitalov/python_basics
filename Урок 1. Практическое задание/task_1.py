
# Задание 1.
# Поработайте с переменными, создайте несколько,выведите на экран, 

variable1 = "1"
variable2 = 1
variable3 = input("Please enter a word:")
variable4 = int(variable1) + variable2

print(variable1)
print(variable2)
print(variable3)
print(f"variable1 + variable2 = {variable4}")

# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
for i in range(3):
    temp_variable = int(input("Please enter a number:"))
    print(f"you entered: {temp_variable}")

#Пример:
#Ведите ваше имя: Василий
#Ведите ваш пароль: vas
#Введите ваш возраст: 45
#Ваши данные для входа в аккаунт: имя - Василий, пароль - vas, возраст - 45

user_data = ["name", "password", "age"]
result = "Your account details : "
for i in user_data:
    request = input(f"please enter {i} : ")
    result += f"{i} - {request} "
print(result)