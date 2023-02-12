hour = 0
minut = 0
sec = int(input("Введите время в секундах:"))
if sec >= 3600 and sec <= 86399:
    hour = sec // 3600
else:
    hour = 00
minut = sec - 3600 * hour
if minut >= 0 and minut <= 3599:
    minut = minut // 60
else:
    minut = 00
sec = sec - 3600 * hour - 60 * minut
print(F"{hour:02}:{minut:02}:{sec:02}")
