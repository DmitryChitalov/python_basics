sec     = float(input("Введите время в сек: "))
hour    = sec / 60 / 60
minutes = sec / 60
print(f"ш{hour:10.1f}:{minutes:10.1f}:{sec:15.1f}")
