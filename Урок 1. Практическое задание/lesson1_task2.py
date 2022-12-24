# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите
# в формате чч:мм:сс. Используйте форматирование строк.

# запрос данных у пользователя
seconds = int(input("Введите время в секундах: "))

# вычисляем число часов, минут, секунд
minutes = seconds // 60
seconds %= 60
hours = minutes // 60
minutes %= 60

# проверяем, возможно ли вывести число в указанном формате
if hours > 99:
    print("Вы ввели слишком большое число, число часов не подходит под формат чч:мм:сс")
else:
    # вычисляем разряды единиц и десятков для секунд, минут, часов
    seconds_1 = seconds % 10
    seconds_10 = seconds // 10
    minutes_1 = minutes % 10
    minutes_10 = minutes // 10
    hours_1 = hours % 10
    hours_10 = hours // 10

    # выводим на экран в формате чч:мм:сс
    print(f'{hours_10}{hours_1}:{minutes_10}{minutes_1}:{seconds_10}{seconds_1}')
