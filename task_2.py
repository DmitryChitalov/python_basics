with open("new_file.txt", "r") as file:
    print(f"Количество строк = "
          f"{len(file.readlines())}")
    file.seek(0)
    i = 0
    for line in file:
        i += 1
        print(f"Количество слов в строке {i} = "
              f"{len(line.split())}")