"""
Задание 6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
.
"""
import random

def guessing_counter(hidden_number):
    attempts = 10

    def in_guessing(hidden):
        nonlocal attempts
        guessed = int(input(f'Введиде число (Осталось {attempts} попыток): '))
        if attempts <= 1:
            return print(
                f'Ты потратил все попытки, загаданное число = {hidden}')
        elif guessed == hidden:
            return print(f'Верно, ты УГАДАЛ число = {hidden}')
        else:
            if guessed > hidden:
                print(f'Ты ввёл число больше загаданного, попробуй ещё раз')
            if guessed < hidden:
                print(f'Ты ввёл число меньше загаданного, попробуй ещё раз')
            attempts -= 1
            return in_guessing(hidden)

    in_guessing(hidden_number)
    return hidden_number


hidden_number = int(random.randint(0, 100))
print(f'Начнём игру ! Я уже загадал число !')
guessing_counter(hidden_number)
