with open("l5t4_file.txt", "w") as numerals:
    line = input("Go on, write some numerals, separated by space ")
    numerals.writelines(line)
res = 0
with open("l5t4_file.txt", "r") as new_file:
    same_list = new_file.read()
    for num in same_list.split():
        res += int(num)
    print(res)


"""
Go on, write some numerals, separated by space 1 2 3 4 5
15
"""
