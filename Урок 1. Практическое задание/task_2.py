my_time = int(input("Введите секунды"))
time_min = my_time // 60
time_hour = time_min // 60
time_sec = my_time % 60
print(f'Время в формате ч:м:с - {time_hour}:{time_min}:{time_sec}')
