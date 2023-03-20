
def num_generator(start, stop):
    for i in range(start, stop):
        yield i


for num in num_generator(3, 10):
    print(num)



from itertools import cycle

my_list = [1, 2, 3]
count = 0

for element in cycle(my_list):
    if count > len(my_list) * 2:
        break
    print(element)
    count += 1
