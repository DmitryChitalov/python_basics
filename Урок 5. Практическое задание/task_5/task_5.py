from task_1.func import write_file

"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

try:
    my_array = []
    my_sum = 0
    for el in range(23):
        my_array.append(str(el + 3))
    write_file("data.txt", ' '.join(my_array))

    with open("data.txt", encoding="utf-8") as f:
        for el in f:
            for number in el.split(' '):
                my_sum += int(number)

    print(f"Сумма чисел в файле: {my_sum}")

except BaseException as e:
    print(f"General error: {e}")

except IOError as e:
    print(f"IOError: {e}")
