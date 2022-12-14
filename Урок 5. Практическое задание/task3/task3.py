my_f = open("salary.txt", "r", encoding='utf-8')
content = my_f.readlines()
my_f.close()
print("Сотрудники с зарплатой < 20k:")
average_income = 0
for el in range(len(content)):
    buffer = content[el].split()
    if float(buffer[1]) < 20000:
        print(buffer[0])
    average_income = average_income + float(buffer[1])
print("Средняя зарплата сотрудников: %.2f" % float(average_income / len(content)))

