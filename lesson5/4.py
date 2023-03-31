"""
Создать (не программно) текстовый файл со следующим содержимым:
One - 1
Two - 2
Three - 3
Four - 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

translations = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре",
    # и так далее ...
}

converted_rows = []

with open("4.txt") as input_data:
    for row in input_data:
        name, value = row.split(' - ')
        converted_rows.append(f"{translations[name]} - {value}")

with open("4_ru.txt", "w") as output_data:
    output_data.writelines(converted_rows)