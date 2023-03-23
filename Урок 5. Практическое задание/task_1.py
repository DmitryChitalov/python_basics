filename = input("Введите имя файла: ")

with open(filename, 'w') as f:
    while True:
        line = input("Введите строку (для выхода оставьте строку пустой): ")
        if not line:
            break
        f.write(line + '\n')
print(f"Данные успешно записаны в файл {filename}")
