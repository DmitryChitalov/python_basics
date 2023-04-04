'''
2. Пользователь вводит время в секундах.
Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
'''

in_seconds = int(input("Введите время в секундах: "))
hours = in_seconds // 3600
rem_hours_seconds = in_seconds - hours * 3600
minutes = rem_hours_seconds // 60
seconds = rem_hours_seconds - minutes * 60
print(f"Время в формате ч:м:с - {hours}:{minutes}:{seconds}")
