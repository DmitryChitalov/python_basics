usr_list = input("Введите целые числа через пробел: ").split()
for a in range(0, len(usr_list)-1, 2):
    usr_list[a], usr_list[a+1] = usr_list[a+1], usr_list[a]
print(f"Результат: {usr_list}")