user_data = input("Введите число: ")
result = 0
i = 0
while (i < len(user_data)):
    if result <= int(user_data[i]):
        result = int(user_data[i])
    i = i + 1
print(f"Наибольшая цифро в веденном числе: {result}")
