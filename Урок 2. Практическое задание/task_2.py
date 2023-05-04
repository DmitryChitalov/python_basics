input_line = input("Enter elements separated by spaces: ")
list1 = input_line.split(' ')
print('Original list: ', list1)

for i in range(1, len(list1), 2):
    input('')
    print(f'i == {i}')
    print(f'Swapping elements "{list1[i - 1]}" and "{list1[i]}"')

    list1[i-1], list1[i] = list1[i], list1[i-1]

input('')
print('New list:    ', list1)
