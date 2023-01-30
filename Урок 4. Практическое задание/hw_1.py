from sys import argv

script_name, first_script, second_script, third_script = argv

print('Имя скрипта: ', script_name)
print('Выработка в часах: ', first_script)
print('Ставка в час: ', second_script)
print('Премия: ', third_script)
print('Зарплата составляет: ', int(first_script) * int(second_script) + int(third_script))
