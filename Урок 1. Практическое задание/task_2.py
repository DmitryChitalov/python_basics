# tack_2

time_sec = int(input('Введите время в секундах: '))
hours = time_sec // 3600
hours_res = (hours) if hours > 10 else ('0' + str(hours))
minutes = (time_sec % 3600) // 60
minutes_res = (minutes) if minutes > 10 else ('0' + str(minutes))
seconds = (time_sec % 3600) % 60
seconds_res = (seconds) if seconds > 10 else ('0' + str(seconds))
if hours > 24:
    print(
        'Количество полученных часов превышает количество часов в сутка, скоректируйте ввод.')
else:
    print(f'Московское время: {hours_res}:{minutes_res}:{seconds_res}')
