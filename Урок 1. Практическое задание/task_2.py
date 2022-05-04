sec = int(input("Секунды: "))
hours = int(sec // 3600) % 24
minutes = int(sec // 60) % 60
seconds = int(sec % 60)
print(str(hours)+":"+str(minutes)+":"+str(seconds))
