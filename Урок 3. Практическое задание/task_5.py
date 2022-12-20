"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
    выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
    нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
    вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
    символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
    ранее сумме и после этого завершить программу.
"""
""" # функция для подсчета суммы цифр
def get_sum(usr_inp):
    result = 0
    for i in range(len(usr_inp)):
        result += int(usr_inp[i])
    return result

temp_res = 0 # сюда будет записываться результат
count = 1 # счетчик для подсчета 

while True:
    user_input = input('Введите цифры: ').split()
    if (temp_res != 0):
        temp_res += get_sum(user_input)
        print (count, 'Сумма чисел = ',temp_res)
    else:
        temp_res = get_sum(user_input)
        print(count, 'Сумма чисел = ', get_sum(user_input))
    count += 1 """
    
#
def get_sum(inp = 0):
    result = 0
    count = 1
    while True:
        user_input = input('Введите цифры: ').split()
        try:
            for i in range(len(user_input)):
                temp_elem = int(user_input[i])
                if type(temp_elem) is int:
                    if (result != 0):
                        result += int(temp_elem)
                    else:
                        result = temp_elem        
            print (f'{count}) Сумма чисел = {result}')
        except ValueError:
            print (f'{count}) Сумма чисел = {result}')
            print('Программа завершена.')
            break
        count += 1

get_sum()



