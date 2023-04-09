numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result_list = [
    val for idx, val in enumerate(numbers)
    if idx > 0 and numbers[idx - 1] < val
]

print(result_list)