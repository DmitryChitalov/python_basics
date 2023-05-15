my_list = [300, 2, 14, 11, 24, 35, 46, 123, 551]
new_list = []

for i in range(1,len(my_list)):
    if my_list[i] > my_list[i-1]:
        new_list.append(my_list[i])

new_list_gen = [el for num, el in enumerate(my_list) if num >= 1 and my_list[num-1] < el]

print('my_list', my_list)
print('new_list', new_list)
print('new_list_gen', new_list_gen)
