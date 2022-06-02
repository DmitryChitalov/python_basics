def my_func(x, y, z):
    sequence = [x, y, z]
    total = []
    max_1 = max(sequence)
    total.append(max_1)
    sequence.remove(max_1)
    max_2 = max(sequence)
    total.append(max_2)
    print(sum(total))


my_func(-4, 2, 0)
