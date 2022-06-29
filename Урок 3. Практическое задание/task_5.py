"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
    выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
    нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
    вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
    символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
    ранее сумме и после этого завершить программу.
"""

numbers_sum = 0


def add_sum(numbers):
    global numbers_sum
    numbers_sum += sum(numbers)
    print(f'Сумма: {numbers_sum}')


while True:
    numbers = input('Введите числа через пробел: ').split(" ")
    only_numbers = list(filter(lambda x: x.isdigit(), numbers))
    only_numbers = [float(itm) for itm in only_numbers]
    if len(numbers) == len(only_numbers):
        add_sum(only_numbers)
    else:
        add_sum(only_numbers)
        print("Выход")
        break
