seconds = int(input("Введите число в секундах: "))
hours = seconds // 3600
seconds = seconds - hours * 3600
minutes = seconds // 60
seconds = seconds - minutes * 60

print(f'Time: {hours:02}:{minutes:02}:{seconds:02}')