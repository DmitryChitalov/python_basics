"""
Задание 6.
В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""
from random import randint

def guess_num(att, const, hid_num):
    
    if att == 0:
        print("Вы не смогли отгадать за {} попыток, число равно {}".format(
           const, hid_num))
        return

    else:
        try:
            num = int(input("Попытка {}. Отгадайте число от 1 до 100: ".format(
                const - att + 1)))
        
        except ValueError:
            print("вы ввели не число, попробуйте еще раз")
            guess_num(att - 1,  const, hid_num)
        else: 
        
            if num == hid_num:
                print("Поздравляем, вы отгадали число c {} попытки! ".format(
                    const - att + 1))
                return
            
            elif num > hid_num:
                print("Загаданное число меньше введенного")
                guess_num(att - 1,  const, hid_num)
            
            else:
                print("Загаданное число больше введенного")
                guess_num(att - 1,  const, hid_num)


hidden_number = randint(0, 100)
attempt = 10  
guess_num(attempt, attempt, hidden_number)