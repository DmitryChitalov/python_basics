"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
    выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
    нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
    вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
    символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
    ранее сумме и после этого завершить программу.
"""
summa = 0
stop = 0
while stop != 1:
    a = input('Введите строку чисел через пробел (для выхода нажмите любою кнопку кроме цифры: ')
    a = a.split()
    for item in a:
        try:
            summa += int(item)
        except:
            stop = 1
    print(summa)
print('Вы закончили программу')






