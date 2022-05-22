#Седьмое задание

a = int(input("Введите количество километров:"))
b = int(input("Цель:"))
count = 1
while a < b:
    print(f'{count} день: {a:.2f}')
    a = a * 1.1
    count += 1
print(f'{count} день: {a:.2f}')
print(f'На {count} день: спортсмен достиг результата -- не менее {a:.2f} км.')