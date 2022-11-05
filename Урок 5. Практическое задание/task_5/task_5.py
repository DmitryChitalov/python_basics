"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from random import randint

gen_nums_count = randint(5, 20)

try:
    gen_nums = [str(randint(-10, 10)) for el in enumerate(range(gen_nums_count))]
    with open("numbers.dat", "w+", encoding="utf-8") as f_obj:
        f_obj.write(" ".join(gen_nums))

        f_obj.seek(0)
        nums_str = f_obj.readline()
        print(f"Сгененрированные числа:\n{nums_str}")

        sum_nums = sum(list(map(int, nums_str.split(" "))))
        print(f"Сумма чисел в файле: {sum_nums}")
except IOError:
    print("Произошла ошибка ввода вывода!")
