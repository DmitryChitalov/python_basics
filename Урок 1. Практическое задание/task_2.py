#Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
 #Используйте форматирование строк.
time_translation = int(input("Введите время в секундах: "))
hour = time_translation // 3600
minute = (time_translation % 3600) // 60
second = (time_translation % 3600) % 60

print(f"{hour:02}:{minute:02}:{second:02}")