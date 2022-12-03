"""
Задание 5 (специальный символ 'e' EN).

Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии Enter должна выводиться сумма чисел. 
Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter. 
Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается. 
Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""
def get_sum(my_str: str):
    sum = 0
    for elem in my_str.split(' '):
        
        if elem.isnumeric():
            sum += int(elem)
        
    return sum


sum_numbers = 0

while True:
    input_str = input('Введите числа: ')

    if not input_str.endswith('e'):
        sum_numbers += get_sum(input_str)
        print('Сумма: ', sum_numbers)
    else:
        last_symbol = input_str[len(input_str) - 1]
        input_str = input_str.replace(last_symbol, '')
        sum_numbers += get_sum(input_str)
        print('Вы ввели специальный симол\nСумма:', sum_numbers)
        break


    