"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
values_list = []
while True:
    user_val = input('Введите число или пустую строку для завершения: ')
    if user_val == '':
        break
    else:
        values_list.append(int(user_val))
values_sum = sum(values_list)
data_to_write = ' '.join(map(str, values_list))
print(f'Сумма введенных значений: {values_sum}')
with open('task_5_result.txt', 'a', encoding='utf-8') as f:
    f.write(data_to_write)
