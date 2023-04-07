one_day = int(input("Введите результат за первый день :"))
result = int(input("Введите требуемый результат :"))
day = 1
while one_day < result:
	day = day + 1
	one_day = one_day + one_day * 0.1
print(f"На {day} день, результат спортсмена составит не менее {round(one_day)} километров")
