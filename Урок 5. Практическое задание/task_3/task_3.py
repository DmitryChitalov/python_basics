"""
4)	Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

IN_FILE = "numbers_en.txt"
OUT_FILE = "numbers_ru.txt"

ru_dict = {"0": "Ноль", "1": "Один", "2": "Два", "3": "Три", "4": "Четыре", "5": "Пять", "6": "Шесть", "7": "Семь",
           "8": "Восемь", "9": "Девять"}

numbers_ru = []

try:
    with open(IN_FILE) as f_en:
        for line_en in f_en:
            num = line_en.split(" - ")[1].rstrip()
            numbers_ru.append(f"{ru_dict.get(num)} - {num}")
except IOError:
    print(f"Произошла ошибка ввода вывода при чтении файла: {IN_FILE}!")

try:
    with open(OUT_FILE, "w", encoding="utf-8") as f_ru:
        print("\n".join(numbers_ru), file=f_ru)
except IOError:
    print(f"Произошла ошибка ввода вывода при записи файла {OUT_FILE}!")


try:
    with open(OUT_FILE, encoding="utf-8") as f_ru:
        print(f"Полученный файл {OUT_FILE}:")
        print(f_ru.read())
except IOError:
    print(f"Произошла ошибка ввода вывода при чтении файла {OUT_FILE}!")
