users_value = int(input("Введите время в секундах "))

a = int(users_value / 60)
h = int(a / 60)
m = int(a % 60)
c = int(users_value % 60)

print (f"{h}:{m}:{c}")



