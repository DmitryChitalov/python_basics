from itertools import count, cycle

# итератор A
print("*" * 20, "Iterator A")
start_iterator = 7

for el in count(start_iterator):
    if el > 10:
        break

    print(el)

# итератор B
print("*" * 20, "Iterator B")
cycling_list = [4, 8, 15, 16, 23, 42]
max_iterations = 12
iteration_count = 0

for el in cycle(cycling_list):
    print(el)
    iteration_count += 1

    if iteration_count >= max_iterations:
        break