with open("task5.txt", "w") as file:
    file.write("1 2 3 4 5")
with open("task5.txt", "r") as file:
    numbers = list(map(int, file.read().split()))
    sum_of_numbers = sum(numbers)
print("Сумма чисел:", sum_of_numbers)
