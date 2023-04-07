numb = int(input("Ведите целое положительное число: "))
max_numb = 0
while numb != 0:
    cur_numb = numb % 10
    if max_numb < cur_numb:
        max_numb = cur_numb
    numb = numb // 10
print(f"Самая большая цифра в числе: {max_numb}")

