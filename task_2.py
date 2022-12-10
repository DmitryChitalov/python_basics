time = int(input("Введите время в секундах: "))
minute = time // 60
hour = minute // 60
print(f"время в часах, минутах и секундах: {hour}:{minute}:{time}")