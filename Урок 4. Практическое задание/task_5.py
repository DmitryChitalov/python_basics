from functools import reduce

even_nums = [num for num in range(100, 1001) if num % 2 == 0]
result = reduce(lambda x, y: x * y, even_nums)

print(result)
