list_1 = input("Cлова через пробел: ").split()
for a, el in enumerate(list_1, 1):
    print(f'{a}. {el[:10]}')
