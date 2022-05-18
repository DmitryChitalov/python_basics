number = int(input("input positive integer: "))
max_num = 0
while number > 0:
    if max_num < number % 10:
        max_num = number % 10
    number = number // 10
print(f"maximum digit is {max_num}")
