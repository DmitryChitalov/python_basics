from functools import reduce

numbers = [item for item in range(100, 1000 + 1) if item % 2 == 0]

multiplication = reduce(lambda x, y: x * y, numbers, 1)

print(multiplication)