"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""






with open("numbers.txt", "w") as f:
    numbers = [1, 2, 3, 4, 5]
    numbers_str = " ".join(str(num) for num in numbers)
    f.write(numbers_str)



with open("numbers.txt", "r") as f:
    numbers_str = f.read()
    numbers = [int(num) for num in numbers_str.split()]
    sum_numbers = sum(numbers)
    print("Сумма чисел в файле: ", sum_numbers)