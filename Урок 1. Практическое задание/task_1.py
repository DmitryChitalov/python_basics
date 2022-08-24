insert = int(input("Введите время в секундах?"))
hours = insert // 3600
minutes = (insert - (hours * 3600)) // 60
seconds = insert - (hours * 3600 + minutes * 60)
print(f'{hours}:{minutes}:{seconds}')
