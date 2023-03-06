user_time = int(input("Введите время в секундах:"))
hours = user_time // 3600
minutes = (user_time - hours * 3600) // 60
seconds = (user_time - hours * 3600) - minutes * 60
print(f'{hours}:{minutes}:{seconds}')