# 2. Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time = int(input('Введите время в секундах: '))
seconds = time%60
minutes = time//60
hours = minutes//60
minutes = minutes - (hours*60)
print(f'{hours:02}:{minutes:02}:{seconds:02}')