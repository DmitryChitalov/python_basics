"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

def my_func1(*args):
    storage = list(args)
    if 3 != len(storage):
        raise Exception("Invalid input data. Should be 3 parameters.")
    for val in storage:
        if int != type(val):
            raise Exception(f"({val} is not integer).")
    storage.sort()
    return storage[1] + storage[2]

def my_func2(*args):
    storage = list(args)
    if 3 != len(storage):
        raise Exception("Invalid input data. Should be 3 parameters.")
    for val in storage:
        if int != type(val):
            raise Exception(f"({val} is not integer).")
    max_val = storage[0]
    for val in storage:
        if val > max_val:
            max_val = val
    min_val = storage[0]
    for val in storage:
        if val < min_val:
            min_val = val
    average_val = 0
    for val in storage:
        if min_val == val or max_val == val:
            continue
        else:
            average_val = val
            break
    return average_val + max_val

print(f"Sum in first case: {my_func1(120, -3, 16)}")
print(f"Sum in second case: {my_func2(120, -3, 16)}")
