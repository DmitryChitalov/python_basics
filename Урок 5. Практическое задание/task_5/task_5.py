"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

my_file = "text5.txt"
digits_str = "21 11.2 35 20.3 5 0 11.5"
if __name__ == "__main__":
    summ = 0

    try:
        with open(my_file, 'w', encoding='utf-8') as fhs:
            fhs.write(digits_str)

        with open(my_file, encoding='utf-8') as fhd:
            data = fhd.read()

        for item in data.split():
            summ += float(item)
    except IOError as e:
        print(e)
    except ValueError:
        print("Неправильно набран номер. Ошибка ввода-вывода")

    print(summ)
