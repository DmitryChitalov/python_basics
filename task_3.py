income = 0
with open("salary.txt", "r", encoding="utf-8") as file:
    for line in file:
        a = line.split()
        income += int(a[1])
        if int(a[1]) < 20000:
            print(f"Сотрудники с окладом ниже 20 тыс. руб.: {a[0]}")
    file.seek(0)
    print(f"Средняя величина дохода = {income / len(file.readlines())}")