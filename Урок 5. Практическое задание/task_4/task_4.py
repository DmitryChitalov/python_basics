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
translate = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре"
}

converted = []

with open("task_4.txt", "r", encoding='utf-8') as f_obj1:
    for i in f_obj1:
        i = i.split(' ', 1)
        converted.append(translate[i[0]] + '  ' + i[1])
with open('task4_ru.txt', 'w+', encoding='utf-8') as f_obj2:
    f_obj2.writelines(converted)
    f_obj2.seek(0)
    cont2 = f_obj2.read()
print("Перевод завершён")
