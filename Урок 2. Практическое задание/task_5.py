list01 = [7, 9, 1, 3, 6, 2, 5]
print('Original list: ', list01)
number = int(input('Enter number: '))

if number <= list01[-1]:
    print(f'{number} <= {list01[-1]}')
    list01.append(number)


else:
    for i in range(len(list01)):
        input('')
        print(f'i == {i}, list01[i] == {list01[i]}')
        if number > list01[i]:
            print(f'{number} > {list01[i]}')
            list01.insert(i, number)
            break

print('New list:    ', list01)