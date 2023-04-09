total = 0

while True:
    user_numbers = input("Введите строку из чисел через пробел >>> ").split()
    has_special_character = False

    for number in user_numbers:
        if number.isdigit():
            total += int(number)
        else:
            has_special_character = True
            break

    print(f"Общая сумма чисел = {total}")

    if has_special_character:
        break