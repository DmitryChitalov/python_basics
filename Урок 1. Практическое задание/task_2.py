number_of_sec = int(input("Введите количество секунд: "))
print("Введено секунд: ", number_of_sec)

sec = number_of_sec % 60  #считаем сколько секунд, отнимаем их от введенного количества

hour = number_of_sec // 3600 #считаем сколько часов, отнимаем их от общего количества
number_of_sec = number_of_sec - hour*3600

min = number_of_sec // 60 #считаем сколько минут

print(f"Пересчитаем (ЧЧ:ММ:СС): {hour:0>2}:{min:0>2}:{sec:0>2}")
