timeC = int(intput("Введите время в секундах:"))
hours = timeC // 3600
minute = timeC // 60
sec = minute * 60
print(f"Время в формате ч:м:с - {hours}, {minute}, {sec}")