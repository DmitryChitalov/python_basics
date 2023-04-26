import datetime
n = int(input("Введите число в секундах: "))
time_format = str(datetime.timedelta(seconds = n))
print("Time in prefffered format :-",time_format)
