with open("2_task.txt", "r", encoding="utf-8") as my_f:
    workers = {}
    for line in my_f:
        key, value = line.split()
        workers[key] = int(value)
        if int(value) < 20000:
            print(f"{key}: зп ниже минимума")
average_value = sum(workers.values()) / len(workers)
print(f"Средняя заработная плата по отделу = {average_value}")


"""
Peter 50000
Sam 55000
Alice 80000
Phoebe 60000
Chandler 70000
Alex 90000
Timy 10000
Eloy 10000
Ron 40000
Harry 70000

Result:
Timy: зп ниже минимума
Eloy: зп ниже минимума
Средняя заработная плата по отделу = 53500.0
"""
