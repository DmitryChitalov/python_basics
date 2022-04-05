mes = int(input("Введите номер месяца"))
season = ["зима", "весна", "лето", "осень"]
uslovie ={1: "зима", 2: "весна", 3: "лето", 4: "осень"}
if mes == 12 or mes == 1 or mes == 2:
    print(uslovie.get(1))
    print(season[0])
elif mes == 3 or mes == 4 or mes == 5:
    print(uslovie.get(2))
    print(season[1])
elif mes == 6 or mes == 7 or mes == 8:
    print(uslovie.get(3))
    print(season[2])
elif mes == 9 or mes == 10 or mes == 11:
    print(uslovie.get(4))
    print(season[3])
else:
    print("нет такого месяца")